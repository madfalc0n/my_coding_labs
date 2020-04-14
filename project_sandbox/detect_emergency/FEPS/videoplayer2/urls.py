from django.urls import path
from . import views

urlpatterns = [
    path('test',views.test),
    path('videoview',views.index, name='videoview'),
]
