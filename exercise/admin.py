from django.contrib import admin
from .models import Exercise, FavouriteExercises

# This registers the exercise app into the admin page
admin.site.register(Exercise)
admin.site.register(FavouriteExercises)