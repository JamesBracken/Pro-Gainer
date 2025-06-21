from django.http import HttpResponse


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
            content=f"Unhandled webhook received: {event["type"]}",
            status=200)
    def handle_payment_intent_succeeded(self, event):
        """ 
        Handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f"Webhook received: {event["type"]}",
            status=200)   
    
    def handle_payment_intent_failed(self, event):
        """ 
        Handle the payment_intent.failed webhook from Stripe
        """
        return HttpResponse(
            content=f"Webhook received: {event["type"]}",
            status=200)   