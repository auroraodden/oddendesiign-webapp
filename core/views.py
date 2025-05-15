from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

from .models import GalleryImage

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})

from .models import Product

def outlet(request):
    products = Product.objects.filter(is_available=True) # Henter kun produkter som er tilgjengelige for kjøp, ikke utgåtte produkter
    return render(request, 'core/outlet.html', {'products': products}) # Sender listen med produkter videre til en egen html-fil