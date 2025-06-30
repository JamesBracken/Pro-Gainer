from django.contrib import admin
from .models import Membership

# Registers the Membership model in the admin page
admin.site.register(Membership)
