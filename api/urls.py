from django.urls import path
from . import views

urlpatterns = [
    path('', views.nothing, name='blank'),
]