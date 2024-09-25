from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login
from auth.forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('account_info')  # Redirect to the account info page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


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
    return redirect('googleMaps:googleMaps')

@login_required
def account_info(request):
    return render(request, 'account_info.html')


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
