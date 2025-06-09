from django.urls import path
from . import views

urlpatterns = [
    path('exercise_list/', views.exercise_list, name='exercise_list'),
]
