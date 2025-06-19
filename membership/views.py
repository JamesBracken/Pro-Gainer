from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import SubscribeForm
from .models import Membership
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from dateutil.relativedelta import relativedelta

import stripe


def checkout(request):
    """
    Render the subscription form for user checkout
    """
    # Checkout code was done alongside the code institute
    # Boutique ado project and tweaked for the needs of this project
    ADD_TOTAL_AMOUNT_HERE_FOR_PAYMENT = 420


    # Stripe variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # Create the stripe intent
    stripe.api_key =  stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=ADD_TOTAL_AMOUNT_HERE_FOR_PAYMENT,
        currency=settings.STRIPE_CURRENCY,
    )
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                         Please make sure the public key is set.')
    is_membership_instance = Membership.objects.filter(user=request.user).exists()

    if request.method == "POST":

        if is_membership_instance:
            membership_instance = Membership.objects.filter(user=request.user).first()
            subscription_form = SubscribeForm(request.POST, instance=membership_instance)
        else:
            subscription_form = SubscribeForm(request.POST)
        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            input_membership_length = int(subscription_form.cleaned_data["membership_length"])
            if is_membership_instance:
                date_today = timezone.now()
                if membership_instance.membership_end_date < date_today:
                    subscription.membership_end_date = timezone.now() + relativedelta(months=input_membership_length)
                elif membership_instance.membership_end_date > date_today:
                    subscription.membership_end_date = membership_instance.membership_end_date + relativedelta(months=input_membership_length)
            else:
                subscription.membership_end_date = timezone.now() + relativedelta(months=input_membership_length)
                subscription.membership_start = timezone.now()
            subscription.user = request.user
            # Setting the membership payment amount
            # selected_subscription_length = int(subscription)
            if input_membership_length == 3:
                membership_instance.last_payment = settings.THREE_MONTH_SUBSCRIPTION_FEE
            if input_membership_length == 12:
                membership_instance.last_payment = settings.TWELVE_MONTH_SUBSCRIPTION_FEE
            subscription_form.save()
            return redirect(reverse("checkout_success"))
        else:
            messages.add_message(request, messages.ERROR, "There is an error in your form.\
                                 Please double check all of your information.")
    else:
        if (is_membership_instance):
            membership_instance = Membership.objects.filter(user=request.user).first()
            subscription_form = SubscribeForm(instance=membership_instance)
        else:
            subscription_form = SubscribeForm()
        
        template = "membership/subscription_form.html"
        context = {
            "subscription_form": subscription_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)

def checkout_success(request):
    """
    Handle successful user checkout
    """
    user_membership = get_object_or_404(Membership, user=request.user)
    user_membership_end_date = user_membership.membership_end_date.strftime("%Y-%m-%d")
    messages.add_message(request, messages.SUCCESS, f"Your payment has been successfully processed! \
                         Your membership will last until {user_membership_end_date}")
    
    template = "membership/checkout_success.html"

    context= {
        "membership": user_membership
    }
    return render(request, template, context)




