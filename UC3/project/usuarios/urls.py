from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name="login"),
]
