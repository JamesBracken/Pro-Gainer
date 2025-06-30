from .models import Membership
from django.utils import timezone


def is_user_membership_active(user):
    """
    Returns a boolean value based on the values stored in the instance
    :model:`membership.Membership`
    """
    if user.is_authenticated:
        membership = Membership.objects.filter(user=user).first()
        if (membership and membership.membership_end_date >= timezone.now()
                and membership.is_member_active):
            return True
    return False
