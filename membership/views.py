from django.shortcuts import render
from .forms import SubscribeForm

# Create your views here.

def checkout(request):
    """
    Render the subscription form for user checkout
    """
    if request.method == "POST":
        return
    else:
        subscription_form = SubscribeForm()
        template = "membership/subscription_form.html"
        context = {
            "subscription_form": subscription_form,
        }

        return render(request, template, context)