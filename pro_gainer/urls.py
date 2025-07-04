"""
URL configuration for pro_gainer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exercise/", include("exercise.urls"), name="exercises"),
    path("membership/", include("membership.urls"), name="memberships"),
    path("", views.index, name="home"),
    path("accounts/", include("allauth.urls")),
]


handler403 = "pro_gainer.views.custom_403"
handler404 = "pro_gainer.views.custom_404"
handler500 = "pro_gainer.views.custom_500"
