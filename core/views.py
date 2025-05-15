from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

from .models import GalleryImage

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})