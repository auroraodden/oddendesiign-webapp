from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('outlet/', views.outlet, name='outlet'), # Kobler URL-en /outlet/ til funksjonen outlet(), da vet Django hvilken visning den skal kjøre når noen besøker den adressen
]
