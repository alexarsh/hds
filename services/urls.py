from django.contrib import admin
from django.urls import path

from services import views

urlpatterns = [
    path('health/', views.health),
    path('availability/', views.availability)
]
