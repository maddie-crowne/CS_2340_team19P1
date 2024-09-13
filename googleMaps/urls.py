from django.urls import path
from . import views

app_name = 'googleMaps'
urlpatterns = [
    path('', views.googleMaps, name='googleMaps'),
]
