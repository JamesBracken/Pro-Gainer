from .models import Membership
from django.utils import timezone


def update_membership_status():
    """
    Automatically updates is_member_active to inactive if the server is running
    and the date now is greater than their membership end date.

    This function updates an instance of :model:`membership.Membership`
    """
    # Written in this manner to avoid data query at
    # import time prior to application configuration
    for membership in Membership.objects.filter(is_member_active=True):
        if membership.membership_end_date < timezone.now():
            membership.is_member_active = False
            membership.save()
