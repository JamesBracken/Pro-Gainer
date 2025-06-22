from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('membership_form/', views.checkout, name='membership_form'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('store_membership_length/', views.store_membership_length, name='store_membership_length'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
