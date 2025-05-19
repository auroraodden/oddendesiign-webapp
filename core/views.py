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

from .models import Review

def reviews_page(request):
    reviews = Review.objects.all() # Henter alle anmeldelser fra databasen
    return render(request, 'core/reviews.html', {'reviews': reviews}) # Sender listen med anmeldelser videre til en egen html-fil (reviews.html)

from .forms import OrderForm

def order_view(request):
    if request.method == 'POST': # Hvis skjemaet ble sendt inn, validerers det og lagres i databasen
        form = OrderForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return render(request, 'core/order_success.html')
    else:
        form = OrderForm()

    return render(request, 'core/order.html', {'form': form}) # Template-filen som skal vise skjemaet