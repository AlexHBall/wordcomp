"""
Required by django
"""
from django.urls import path
from .views import (
    home_view,
)

app_name = 'dict'
urlpatterns = [
    path('', home_view, name='home'),
]