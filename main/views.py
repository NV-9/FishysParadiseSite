from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
import requests
from .models import FPUser


def home_view(request: HttpRequest):
    context = {'invite': settings.INVITE, 'github': settings.GITHUB}
    return render(request, 'main/home.html', context = context)

@login_required(login_url='/oauth2/login')
def dashboard_view(request: HttpRequest):
    context = {}
    if request.user.is_authenticated:
        if isinstance(request.user, FPUser):
            context = {

            }
            return render(request, 'main/dashboard.html', context = context)
    return redirect('home')

def discord_login_view(request: HttpRequest):
    return redirect(settings.AUTH_URL)

def discord_login_redirect_view(request: HttpRequest):
    code = request.GET.get('code', None)
    if not code:
        return redirect('home')
    
    data = {
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.REDIRECT_URI,
        'scope': settings.SCOPES
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post("https://discord.com/api/oauth2/token", data = data, headers = headers)
    credentials = response.json()
    if 'access_token' not in credentials:
        return redirect('/')
    response = requests.get("https://discord.com/api/v6/users/@me", headers = {'Authorization': 'Bearer ' + credentials['access_token']})
    fpuser: FPUser = authenticate(request, user = response.json())
    login(request, user = fpuser)
    return redirect('dashboard')

def logout_view(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
