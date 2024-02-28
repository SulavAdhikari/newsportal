# myapp/urls.py
from django.urls import path
from .views import register, user_login, logout_view, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='user_profile')
    # Add other urlpatterns as needed
]
