from django.contrib import admin
from django.urls import path, include

from users.views import (
    LoginView, 
    RegisterView, 
    logoutView,
    MyProfileView,
)

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logoutView.as_view(), name='logout'),
    path('my_profile', MyProfileView.as_view(), name='my_profile'),
]