from django.urls import path
from . import views

urlpatterns = [
    path('membership_form/', views.checkout, name='membership_form'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
]
