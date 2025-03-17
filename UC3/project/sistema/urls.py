from django.urls import path
from sistema import viws

urlpatterns = [
    path('sistema/', viws.index),
]