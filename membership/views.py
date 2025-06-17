from django.shortcuts import render, redirect
from .forms import SubscribeForm
from django.conf import settings
from django.contrib import messages

import stripe
# Create your views here.

def checkout(request):
    """
    Render the subscription form for user checkout
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    ADD_TOTAL_AMOUNT_HERE_FOR_PAYMENT = 120
    stripe.api_key =  stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=ADD_TOTAL_AMOUNT_HERE_FOR_PAYMENT,
        currency=settings.STRIPE_CURRENCY,
    )
    

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                         Please make sure the public key is set.')

    if request.method == "POST":
        subscription_form = SubscribeForm(request.POST)
        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            subscription.user = request.user
            subscription.membership_start = None
            subscription.next_payment_date = None
            subscription_form.save()
            return redirect("home")
    else:
        subscription_form = SubscribeForm()
        template = "membership/subscription_form.html"
        context = {
            "subscription_form": subscription_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)