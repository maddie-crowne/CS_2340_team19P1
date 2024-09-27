from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.decorators.http import require_http_methods
from auth.forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from googleMaps.models import Favorite


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('googleMaps:googleMaps')  # Redirect to the Google Maps page
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Please correct the errors below.')
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

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('googleMaps:googleMaps')

@login_required
def account_info(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user)
        return render(request, 'account_info.html', {'user': request.user, 'favorites': favorites})
    else:
        return redirect('auth:login')  # Redirect to login if not authenticated


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

import json
import logging  # Import logging
from django.contrib.auth.decorators import login_required

# Set up logging
logger = logging.getLogger(__name__)

@login_required
def favorite(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            place_id = data.get('placeId')

            if not place_id:
                return JsonResponse({'success': False, 'message': 'Place ID is required.'}, status=400)

            # Check if the restaurant is already favorited
            favorite, created = Favorite.objects.get_or_create(user=request.user, place_id=place_id)

            if created:
                return JsonResponse({'success': True, 'message': 'Restaurant favorited!'})
            else:
                # If it exists, delete it (unfavorite)
                favorite.delete()
                return JsonResponse({'success': True, 'message': 'Restaurant unfavorited!'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            logger.error(f"Error favoriting/unfavoriting restaurant: {str(e)}")  # Log the error
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@require_http_methods(["DELETE"])
@login_required
def unfavorite(request, place_id):
    try:
        favorite = Favorite.objects.get(user=request.user, place_id=place_id)
        favorite.delete()
        return JsonResponse({'success': True})
    except Favorite.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Favorite not found.'})

@login_required  # Ensure the user is logged in
def is_favorited(request, place_id):
    user = request.user
    # Check if the place_id is in the user's favorites
    is_favorited = Favorite.objects.filter(user=user, place_id=place_id).exists()
    return JsonResponse({'isFavorited': is_favorited})