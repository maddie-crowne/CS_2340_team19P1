from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def account_info(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'account_info.html', {'favorites': favorites})


# Create your views here.
def googleMaps(request):
    return render(request, 'googleMaps.html', {
        'google_maps_api_key': settings.API_KEY
    })
def map_proxy(request):
    api_url = 'https://maps.googleapis.com/maps/api/js'
    params = {
        'key': settings.API_KEY,
        'libraries': 'maps',
        'v': 'beta'
    }
    response = requests.get(api_url, params=params)
    return JsonResponse(response.json())
