from django.urls import path
from . import views

urlpatterns = [
    path('toggle-meal-status/', views.toggle_meal_status, name='toggle_meal_status'),
    path('request-meal-for-night/', views.request_meal_for_night, name='request_meal_for_night'),
    path('recharge/<int:user_id>/', views.recharge_account, name='recharge_account'),
    path('toggle-user-meal/<int:user_id>/', views.toggle_user_meal_status, name='toggle_user_meal_status'),
]