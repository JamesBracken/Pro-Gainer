from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubscribeForm
from .models import Membership
from django.conf import settings
from django.contrib import messages

import stripe
# Create your views here.

def checkout(request):
    """
    Render the subscription form for user checkout
    """
    # Checkout code was done alongside the code institute
    # Boutique ado project and tweaked for the needs of this project
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    ADD_TOTAL_AMOUNT_HERE_FOR_PAYMENT = 420
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
        if (is_membership_instance):
            membership_instance = Membership.objects.filter(user=request.user).first()
            subscription_form = SubscribeForm(request.POST, instance=membership_instance)
        else:
            subscription_form = SubscribeForm(request.POST)

        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            subscription.user = request.user
            subscription.membership_start = None
            subscription.next_payment_date = None
            subscription_form.save()
            return redirect("home")
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