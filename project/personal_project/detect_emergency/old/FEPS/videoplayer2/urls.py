from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    path('videoview1', views.index, name='videoview1'),
    path('videoview2', views.index2, name='videoview2'),
]
