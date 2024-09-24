from django.urls import path
from . import views

app_name = 'googleMaps'
urlpatterns = [
    path('', views.googleMaps, name='googleMaps'),
    path('account/', views.account_info, name='account_info'),  # User's account info page
]
