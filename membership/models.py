from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Membership(models.Model):
    """
    Stores a membership entry related to :model:`auth.user`.
    """

    # Choices for gym locations
    GYM_LOCATIONS = [
        ("Hounslow", "Hounslow"),
    ]
    # Choices for membership types
    MEMBERSHIP_TYPES = [
        ("Regular", "Regular"),
    ]

    # General user details models is based off of the Code Institute
    # Boutique Ado project. Obviously this information is used across
    # majority of sites so not much if any tweaking involved
    # Similarly we would like to have the user data for later uses like
    # potential ads, promotions etc.

    # User details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email_address = models.EmailField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    # User Address details
    country = CountryField(max_length=100, null=False, blank=False)
    post_code = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=100, null=False, blank=False)
    street_address_1 = models.CharField(max_length=200,
                                        null=False, blank=False)
    street_address_2 = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=70, null=False, blank=False)

    # The below models are for use in the functionality of the website
    # and potential future upgrades
    # Membership details
    membership_start_date = models.DateTimeField(null=True)
    gym_location = models.CharField(choices=GYM_LOCATIONS)
    membership_type = models.CharField(choices=MEMBERSHIP_TYPES)
    is_member_active = models.BooleanField(default=False)
    membership_end_date = models.DateTimeField(null=True)
    last_payment = models.IntegerField(null=True)
