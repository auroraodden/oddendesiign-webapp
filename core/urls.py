from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('outlet/', views.outlet, name='outlet'), # Kobler til /outlet/-funksjonen i views.py
    path('reviews/', views.reviews_page, name='reviews'), # Kobler til /reviews/-funksjonen i views.py
]
