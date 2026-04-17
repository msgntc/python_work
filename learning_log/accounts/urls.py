"""Defines URL patterns for accounts"""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # include defoult auth urls
    path('', include('django.contrib.auth.urls')),
    # regastration page
    path('register/', views.register, name='register'),
]