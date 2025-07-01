# user_account/urls.py
from django.urls import path
from .views import ProfileUpdateView

urlpatterns = [
    path('profile', ProfileUpdateView.as_view(), name='profile-update'),
]
