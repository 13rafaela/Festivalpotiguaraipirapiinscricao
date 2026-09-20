from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
]