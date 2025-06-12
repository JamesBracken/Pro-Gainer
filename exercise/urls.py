from django.urls import path
from . import views

urlpatterns = [
    path('exercise_list/', views.exercise_list, name='exercise_list'),
    path('<exercise_slug>', views.exercise_detail, name='exercise_detail'),
    path('add_exercise_item/', views.add_exercise_item, name='add_exercise_item'),
]
