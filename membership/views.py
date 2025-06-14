from django.shortcuts import render, redirect
from .forms import SubscribeForm

# Create your views here.

def checkout(request):
    """
    Render the subscription form for user checkout
    """
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
        }

        return render(request, template, context)