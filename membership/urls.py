from django.urls import path
from . import views

urlpatterns = [
    path('membership_form/', views.checkout, name='membership_form'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('store_membership_length/', views.store_membership_length, name='store_membership_length'),
    path('my_profile/', views.my_profile, name='my_profile'),
]
