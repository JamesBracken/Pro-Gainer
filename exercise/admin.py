from django.contrib import admin
from .models import Exercise

# This registers the exercise app into the admin page
admin.site.register(Exercise)