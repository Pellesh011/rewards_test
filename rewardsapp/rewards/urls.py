from django.contrib import admin
from django.urls import path
from .views import reward_list, request_reward

urlpatterns = [
    path('rewards/request', request_reward, name='request_reward'),
    path('rewards', reward_list, name='reward_list'),
]
