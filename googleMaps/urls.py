from django.urls import path
from . import views

app_name = 'googleMaps'  # Namespacing the app for better URL organization
urlpatterns = [
    path('', views.googleMaps, name='googleMaps'),
    path('register/', views.register, name='register'),
    path('account/', views.account_info, name='account_info'),  # User's account info page
]
