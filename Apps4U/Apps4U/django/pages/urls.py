from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('starter_pack/', views.starter_pack, name='starter_pack'),
]
