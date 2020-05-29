from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('listuser', views.listuser),
    path('tester', views.tester),
]
