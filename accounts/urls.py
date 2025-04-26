from django.urls import path
from .views import (
    login_view, register_view, welcome_view, custom_logout,
    api_login, api_register, api_logout  # <-- added api_logout here
)

urlpatterns = [
    # HTML views
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('welcome/', welcome_view, name='welcome'),
    path('logout/', custom_logout, name='logout'),

    # API endpoints
    path('api/login/', api_login, name='api-login'),
    path('api/register/', api_register, name='api-register'),
    path('api/welcome/', welcome_view, name='api-welcome'),
    path('api/logout/', api_logout, name='api-logout'),  # <-- FIXED to api_logout
]
