from django import forms
from .models import Membership


class SubscribeForm(forms.ModelForm):
    """
    Creates a form for :model:`membership.Membership`
    """


    class Meta:
        model = Membership
        fields = (
            "full_name",
            "email_address",
            "phone_number",
            "country",
            "post_code",
            "town_or_city",
            "street_address_1",
            "street_address_2",
            "county",
            "gym_location",
            "membership_type",
        )

    # "user"
    # ,"full_name"
    # ,"email_address"
    # ,"phone_number"
    # ,"country"
    # ,"post_code"
    # ,"town_or_city"
    # ,"street_address_1"
    # ,"street_address_2"
    # ,"country"

    # # The below models are for use in the functionality of the website
    # # and potential future upgrades
    # gym_location
    # membership_type
    # is_member_active
    # membership_start
    # next_payment_date
