from django.urls import path
from . import views
from googleMaps.views import account_info

app_name = 'auth'

urlpatterns = [
    path('account/', account_info, name='account_info'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]