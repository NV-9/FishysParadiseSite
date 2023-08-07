from django.urls import path 
from .views import *

urlpatterns = [
    path('', home_view, name = 'home'),
    path('dashboard', dashboard_view, name = 'dashboard'),
    path('logout', logout_view, name = 'logout'),
    path('oauth2/login', discord_login_view, name = 'login'),
    path('oauth2/login/redirect', discord_login_redirect_view, name = 'redirect'),
]