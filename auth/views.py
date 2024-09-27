from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm  # Make sure this import is correct
import json

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('googleMaps:googleMaps')  # Redirect to the Google Maps page
        else:
            # Iterate over form errors and add to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('googleMaps:googleMaps')  # Redirect to the Google Maps page
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('auth:login')  # Redirect to login page after logout

@login_required  # Ensure user is logged in
def current_user(request):
    return JsonResponse({'userId': request.user.id})  # Or return any other relevant user info
