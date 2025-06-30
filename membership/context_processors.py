from .utils import is_user_membership_active


def check_member_status(request):
    """
    Returns a boolean value using the logic in
    utils.is_user_membership_active

    **Context**

    ``is_member_active``
        Stores a boolean value based on the instance stored in
        :model:`membership.Membership`
    """
    return {"is_member_active": is_user_membership_active(request.user)}
