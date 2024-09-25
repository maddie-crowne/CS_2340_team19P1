from django.urls import path
from . import views

app_name = 'googleMaps'

urlpatterns = [
    path('', views.googleMaps, name='googleMaps'),
    path('register/', views.register, name='register'),
    path('account/', views.account_info, name='account_info'),
    path('logout/', views.user_logout, name='logout'),  # Correct logout path
]
