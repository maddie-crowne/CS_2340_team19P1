from django.urls import path
from . import views
from .views import favorite, unfavorite

app_name = 'googleMaps'

urlpatterns = [
    path('', views.googleMaps, name='googleMaps'),
    path('register/', views.register, name='register'),
    path('account/', views.account_info, name='account_info'),
    path('logout/', views.user_logout, name='logout'),  # Correct logout path
    path('api/favorite/', favorite, name='favorite_restaurant'),
    path('api/unfavorite/<str:place_id>/', unfavorite, name='unfavorite'),
]
