from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('auth:login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Debugging print statement
        print(f"User: {user}")  # Check if user is None or a valid user object

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
