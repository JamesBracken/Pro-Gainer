from .models import Membership
from django.utils import timezone

def check_member_status(request):
    if request.user.is_authenticated:
        membership = Membership.objects.filter(user=request.user).first()
        if membership and membership.membership_end_date >= timezone.now():
            return{"is_member_active": True }
    return{"is_member_active": False }
