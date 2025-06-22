from django.http import HttpResponse
from .models import Membership
from dateutil.parser import isoparse

import time
import stripe


# Coded along with code institute boutique ado project for the below hanlder
class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event["type"]}", status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        membership = None
        order_exists = False
        attempt = 1
        metadata = event['data']['object']['metadata']
        membership_end_date = intent.metadata.membership_end_date
        membership_start_date_raw = metadata.get("membership_start_date")
        membership_end_date_raw = metadata.get("membership_end_date")

        membership_start_date = isoparse(membership_start_date_raw)
        membership_end_date = isoparse(membership_end_date_raw)


        while attempt <= 5:
            # Searches for an object which matches the below data
            try:
                membership = Membership.objects.get(
                    full_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                )
                order_exists = True
                break
            except Membership.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f"Webhook received: {event["type"]} | SUCCESS : Verified order already in database",
                status=200,
            )
        else:
            # If the order with the above data could not be found then
            # Create one instead with the below data
            order = None
            try:
                user_id = intent.metadata.get("user_id")
                user = None
                if user_id:
                    try:
                        from django.contrib.auth import get_user_model

                        User = get_user_model()
                        user = User.objects.get(id=user_id)
                    except User.DoesNotExist:
                        return HttpResponse(
                            content=f"Webhook received: {event['type']} | ERROR: User with id {user_id} does not exist",
                            status=400,
                        )
                print("User ID from metadata:", user_id)
                print("Metadata:", intent.metadata)
                membership = Membership.objects.create(
                    user=user,
                    full_name=shipping_details.name,
                    email_address=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    post_code=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                )
            except Exception as e:
                if membership:
                    membership.delete()
                return HttpResponse(
                    content=f"Webhook received: {event["type"]} | ERROR: {e}",
                    status=500,
                )
        return HttpResponse(
            content=f"Webhook received: {event["type"]} | SUCCESS: Created order in webhook",
            status=200,
        )

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """
        return HttpResponse(content=f"Webhook received: {event["type"]}", status=200)
