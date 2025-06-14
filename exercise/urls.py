from django.urls import path
from . import views

urlpatterns = [
    path('exercise_list/', views.exercise_list, name='exercise_list'),
    path('<exercise_slug>', views.exercise_detail, name='exercise_detail'),
    path('add_exercise_item/', views.add_exercise_item, name='add_exercise_item'),
    path('edit_exercise_item/<exercise_slug>', views.edit_exercise_item, name='edit_exercise_item'),
    path('delete_exercise_item/<exercise_slug>', views.delete_exercise_item, name='delete_exercise_item'),
    path('favourite_exercise_list/', views.favourite_exercise_list, name='favourite_exercise_list'),
    path('add_favourite_exercise/<exercise_id>', views.add_favourite_exercise, name='add_favourite_exercise'),
]
