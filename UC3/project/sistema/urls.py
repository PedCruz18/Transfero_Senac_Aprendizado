from django.urls import path
from sistema import views

urlpatterns = [
    path('', views.index),
    path('apresentacao/', views.apresentacao),
]