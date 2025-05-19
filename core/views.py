from django.shortcuts import render
from .forms import OrderForm 
from .models import Customer, GalleryImage, Product, Review
from django.core.mail import send_mail

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

from .models import Customer  # Legg denne øverst i filen om den ikke er der

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            send_mail(
                subject='Bekreftelse på bestilling hos Oddendesiign 🎨',
                message=f'Takk for din bestilling, {order.full_name}!\n\n'
                f'Produkt: {order.product.title}\n'
                f'Totalpris: {order.total_price} kr\n\n'
                f'Vi tar kontakt med deg så snart som mulig.\n\n'
                f'Mvh,\nOddendesiign',
                from_email=None,  # bruker DEFAULT_FROM_EMAIL fra settings.py
                recipient_list=[order.email],  # kunden mottar e-posten
                fail_silently=False,
                )

            # Opprett ny Customer basert på info i skjemaet
            customer = Customer.objects.create(
                group_name=order.group_name,
                contact_email=order.email,
                contact_phone=order.phone,
                address=order.address,
            )

            # Koble customer til order
            order.customer = customer

            # Sett total_price basert på valgt produkt
            if order.product:
                order.total_price = order.product.price

            order.save()
            return render(request, 'core/order_success.html')
    else:
        form = OrderForm()
    return render(request, 'core/order.html', {'form': form})