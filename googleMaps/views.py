from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import requests

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
