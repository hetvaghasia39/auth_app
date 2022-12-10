"""app URL Configuration
"""
from django.urls import path
from app.views import *

urlpatterns = [
    path("signup/", Signup.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("profile/<int:pk>/", UserProfile.as_view(), name="profile"),
    path("edit/<int:pk>/", EditProfile.as_view(), name="edit"),
    path("delete/<int:pk>/", DeleteProfile.as_view(), name="delete"),
]
