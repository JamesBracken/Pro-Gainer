from django.urls import path
from . import views

urlpatterns = [
    path('membership_form/', views.checkout, name='membership_form'),
]
