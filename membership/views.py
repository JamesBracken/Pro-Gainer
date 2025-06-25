from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .forms import SubscribeForm
from .models import Membership
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

import stripe
import json


@require_POST
def cache_checkout_data(request):
    membership_instance = Membership.objects.filter(user=request.user).first()

    membership_end_date = calculate_membership_end_date(request, membership_instance)
    # Set the membership start date
    membership_start_date = None
    membership_start_date_str = None
    # membership_start_date is being passed as not timezone aware
    # making this timezone aware here
    if membership_instance and membership_instance.membership_start_date:
        membership_start_date = membership_instance.membership_start_date
        if timezone.is_naive(membership_start_date):
            membership_start_date = timezone.make_aware(membership_start_date)
        membership_start_date_str = membership_start_date.isoformat()
    else:
        membership_start_date_str = timezone.now().isoformat()
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        gym_location = request.POST.get("gym_location", "")
        membership_type = request.POST.get("membership_type", "")
        intent = stripe.PaymentIntent.modify(
            pid,
            metadata={
                "user_id": str(request.user.id),
                "username": str(request.user.username),
                "membership_end_date": str(membership_end_date),
                "gym_location": str(gym_location),
                "membership_type": str(membership_type),
                "membership_start_date": membership_start_date_str,
            },
        )
        print("cache_checkout_data invoked PID:", intent.id)
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot \
                       be processed right now. Please try again later",
        )
    return HttpResponse(content=0, status=400)


def checkout(request):
    """
    Takes session information to update stripe payment amount.

    Render the subscription form for user checkout.

    If the user does not have an instance of :model:`membership.Membership`
    this view will create one

    If the user has an existing instance of :model:`membership.Membership`
    this view will update it

    **Context**

    ``subscription_form``
        An instance of :forms:`membership.SubscribeForm`

    ``stripe_public_key``
        This is the public key used for stripe payments

    ``client_secret``
        This is the client secret used for stripe payments

    **Template**

    ``subscription_form.html``

    """

    print("Session keys:", list(request.session.keys()))
    print("payment_intent_id in session:", "payment_intent_id" in request.session)

    # Checkout code was done alongside the code institute
    # Boutique ado project and tweaked for the needs of this project
    selected_membership_length = request.session.get("selected_membership_length")
    membership_fee = 30
    if isinstance(selected_membership_length, str):
        numified_membership_length = int(selected_membership_length)
        if numified_membership_length == 3:
            membership_fee = settings.THREE_MONTH_SUBSCRIPTION_FEE
        elif numified_membership_length == 12:
            membership_fee = settings.TWELVE_MONTH_SUBSCRIPTION_FEE
    joining_fee = settings.JOINING_FEE
    # Stripe variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # # Create the stripe intent
    stripe.api_key = stripe_secret_key
    # intent = stripe.PaymentIntent.create(
    #         amount=(membership_fee * 100 + joining_fee * 100),
    #         currency=settings.STRIPE_CURRENCY,
    #     )

    # TEST CODE

    # Retrieve or create a PaymentIntent only if necessary
    if "payment_intent_id" in request.session:
        try:
            intent = stripe.PaymentIntent.retrieve(request.session["payment_intent_id"])
            # Incase of any used/old id's left in the session check if this
            # intent has already succeeded or has been cancelled
            if intent.status in ["succeeded", "canceled"]:
                del request.session["payment_intent_id"]
                raise stripe.error.InvalidRequestError(
                    "Old PaymentIntent not reusable", None
                )
        # print("Reusing existing PID from session:", intent.id)
        except stripe.error.InvalidRequestError:
            # If session contains invalid PaymentIntent, create a new one
            intent = stripe.PaymentIntent.create(
                amount=(membership_fee * 100 + joining_fee * 100),
                currency=settings.STRIPE_CURRENCY,
            )
            request.session["payment_intent_id"] = intent.id
            print("Created new PID if payment_intent_id block > except:", intent.id)
    else:
        intent = stripe.PaymentIntent.create(
            amount=(membership_fee * 100 + joining_fee * 100),
            currency=settings.STRIPE_CURRENCY,
        )
        request.session["payment_intent_id"] = intent.id
        print("Created new PID else payment_intent_id block:", intent.id)

    # END OF TEST CODE

    print("Checkout function invoked, paymentIntentId: ", intent.id)
    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing. \
                         Please make sure the public key is set.",
        )
    is_membership_instance = Membership.objects.filter(user=request.user).exists()

    if request.method == "POST":
        print("Checkout function invoked POST block top, paymentIntentId: ", intent.id)
        try:
            updated_amount = membership_fee * 100 + joining_fee * 100
            intent = stripe.PaymentIntent.modify(intent.id, amount=updated_amount)
            print("Modified PI amount:", updated_amount)
        except stripe.error.InvalidRequestError as e:
            print("Stripe error PI.modify at checkout POST block > try:", e)
            messages.error(
                request, "There was an error updating your payment. Please try again."
            )
            return redirect("checkout")
        if is_membership_instance:
            membership_instance = Membership.objects.filter(user=request.user).first()
            subscription_form = SubscribeForm(
                request.POST, instance=membership_instance
            )
            print(
                "Checkout function invoked POST block > if is_membership_instance block, paymentIntentId: ",
                intent.id,
            )

        else:
            subscription_form = SubscribeForm(request.POST)
            # Setting this to none for calculate_membership_end_date calculation
            # parameter, if this is none this parameter would also not be needed
            membership_instance = None
        if subscription_form.is_valid():
            membership_end_date = calculate_membership_end_date(
                request, membership_instance
            )

            subscription = subscription_form.save(commit=False)
            subscription.membership_end_date = membership_end_date
            if is_membership_instance:
                subscription.membership_start = timezone.now()
            subscription.last_payment = membership_fee
            subscription.user = request.user
            subscription.is_member_active = True
            # Temporarily removed setting membership end date
            print(
                "Checkout function invoked POST block > if form.is_valid, paymentIntentId: ",
                intent.id,
            )
            subscription_form.save()
            # Clear stale sessions used to store the user input membership
            del request.session["selected_membership_length"]
            return redirect(reverse("checkout_success"))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "There is an error in your form.\
                                 Please double check all of your information.",
            )
    else:

        # Create the stripe intent
        # stripe.api_key = stripe_secret_key
        # intent = stripe.PaymentIntent.create(
        #         amount=(membership_fee * 100 + joining_fee * 100),
        #         currency=settings.STRIPE_CURRENCY,
        #     )
        if is_membership_instance:
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
    Handle successful user checkout and displays the checkout success page

    **Context**

    ``membership``
        An instance of :model:`membership.Membership`

    ``last_payment``
        An instance of :model:`membership.Membership.last_payment`

    ``joining_fee``
        A variable set in `settings.JOINING_FEE`

    **Template**

    ``checkout_success.html``
    """
    if "payment_intent_id" in request.session:
        del request.session["payment_intent_id"]
    user_membership = get_object_or_404(Membership, user=request.user)
    user_membership_end_date = user_membership.membership_end_date.strftime("%Y-%m-%d")
    user_membership_last_payment = user_membership.last_payment
    JOINING_FEE = settings.JOINING_FEE
    messages.add_message(
        request,
        messages.SUCCESS,
        f"Your payment has been successfully processed! \
                         Your membership will last until {user_membership_end_date}",
    )
    template = "membership/checkout_success.html"

    context = {
        "membership": user_membership,
        "last_payment": user_membership_last_payment,
        "joining_fee": JOINING_FEE,
    }

    return render(request, template, context)


def store_membership_length(request):
    """
    Stores the user selected membership length in a session
    """
    data = json.loads(request.body)
    request.session["selected_membership_length"] = data.get(
        "selected_membership_length"
    )
    # Setting the session status to modified to ensure django commits this session
    request.session.modified = True

    return JsonResponse(
        {
            "status": "ok",
        }
    )


def my_profile(request):
    """
    Display an instance of :model:`membership.Membership`

    **Context**

    ``membership``
        An instance of :model:`membership.Membership`

    **Template**

    ``my_profile.html``
    """
    membership = get_object_or_404(Membership, user=request.user)
    template = "membership/my_profile.html"
    context = {"membership": membership}
    return render(request, template, context)


def calculate_membership_end_date(request, membership_instance):
    is_membership_instance = bool(membership_instance)
    selected_membership_length = int(request.session.get("selected_membership_length"))
    if is_membership_instance:
        date_today = timezone.now()
        membership_end_date = None
        if membership_instance.membership_end_date < date_today:
            membership_end_date = timezone.now() + relativedelta(
                months=selected_membership_length
            )
        elif membership_instance.membership_end_date > date_today:
            membership_end_date = (
                membership_instance.membership_end_date
                + relativedelta(months=selected_membership_length)
            )
        return membership_end_date
    else:
        membership_end_date = timezone.now() + relativedelta(
            months=selected_membership_length
        )
        return membership_end_date
