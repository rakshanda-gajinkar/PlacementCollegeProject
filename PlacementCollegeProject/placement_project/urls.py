from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from api import views  # Import your updated views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Connect your 3 core authentications
    path('', views.index, name='index'), # Root address http://127.0.0.1:8000/ landing page path
    path('',include('api.urls')),
    
]