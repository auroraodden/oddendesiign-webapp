from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('outlet/', views.outlet, name='outlet'), # Kobler til /outlet/-funksjonen i views.py
    path('reviews/', views.reviews_page, name='reviews'), # Kobler til /reviews/-funksjonen i views.py
    path('order/', views.order_view, name='order'), # Kobler til /order/-funksjonen i views.py
    path('teaservideo/', views.teaser_video_view, name='teaser_video'), # Kobler til /teaservideo/-funksjonen i views.py
    path('teaservideo/success/', lambda request: render(request, 'core/teaser_video_success.html'), name='teaser_video_success'),
    path("outlet/order/<int:product_id>/", views.outlet_order_view, name="outlet_order"),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', lambda request: render(request, 'core/contact_success.html'), name='contact_success'),
    path('faq/', views.faq_view, name='faq'), # Kobler til /faq/-funksjonen i views.py
]
