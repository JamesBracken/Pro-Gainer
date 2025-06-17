from django import forms
from .models import Membership


class SubscribeForm(forms.ModelForm):
    """
    Creates a form for :model:`membership.Membership`
    """
    
    # Choices for membership length in months
    MEMBERSHIP_LENGTH = [
            (None, "--------"),
            ("3", "3 Months"),
            ("12", "12 Months"),
    ]
    membership_length = forms.ChoiceField(choices=MEMBERSHIP_LENGTH, required=True, label="Desired Membership Length")
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
# for loop to add a class to each field
    def __init__(self, *args, **kwargs):
        """
        Add classes to each field
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "stripe-style-input"