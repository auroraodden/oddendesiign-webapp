from django.shortcuts import render
from .forms import OrderForm 
from .models import Customer, GalleryImage, Product, Review, UploadedFile
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import TeaserVideoForm
from .models import TeaserVideoFile
from django.conf import settings

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
    reviews = Review.objects.filter(is_approved=True) # Kun godkjente anmeldelser vises
    return render(request, 'core/reviews.html', {'reviews': reviews}) # Sender listen med anmeldelser videre til en egen html-fil (reviews.html)

from .models import Customer  # Legg denne øverst i filen om den ikke er der

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)

            # 1. Opprett Customer
            customer = Customer.objects.create(
                group_name=order.group_name,
                contact_email=order.email,
                contact_phone=order.phone,
                address=order.address,
            )
            order.customer = customer

            # 2. Sett totalpris
            if order.product:
                order.total_price = order.product.price

            # 3. Lagre bestillingen
            order.save()

            # 4. Lagre opplastede filer
            files = request.FILES.getlist('uploaded_files')
            for f in files:
                UploadedFile.objects.create(order=order, file=f)

            # Nå er alt lagret -> sender HTML-e-post
            html_message = render_to_string('core/emails/order_confirmation.html', {'order': order})
            email = EmailMessage(
                subject='Bekreftelse på bestilling hos Oddendesiign 🎨',
                body=html_message,
                from_email=None,
                to=[order.email], # Kunden mottar e-posten
                bcc=['oddendesign@gmail.com'], # Jeg får en skjult kopi
            )
            email.content_subtype = "html"

            if order.uploaded_files: # Hvis kunden har lastet opp en fil
                email.attach_file(order.uploaded_files.path) # Legger ved filen som ble lastet opp

            email.send()

            return render(request, 'core/order_success.html')  # Viser en egen side for bekreftelse av bestilling
    else:
        form = OrderForm()

    return render(request, 'core/order.html', {'form': form})

def teaser_video_view(request):
    if request.method == 'POST':
        form = TeaserVideoForm(request.POST)
        files = request.FILES.getlist('files')  # Henter listen med filer fra skjemaet

        if form.is_valid():
            teaser = form.save()
            for f in files:
                TeaserVideoFile.objects.create(teaser_video=teaser, file=f)
            
            # Send e-postbekreftelse
            subject = f"Bekreftelse på teaservideo-bestilling - {teaser.group_name}"
            message = (
                f"Hei {teaser.full_name}!\n\n"
                f"Takk for at du bestilte teaservideoen «{teaser.product}» hos Oddendesiign 🎬\n\n"
                f"Vi har registrert:\n"
                f"• Gruppenavn: {teaser.group_name}\n"
                f"• E-post: {teaser.email}\n"
                f"• Telefon: {teaser.phone}\n"
                f"• Totalpris: {teaser.total_price} kr\n\n"
                f"Vi tar kontakt når videoen er under produksjon.\n\n"
                f"Hilsen,\nOddendesiign"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [teaser.email],
                fail_silently=False,
            )

            return redirect('teaser_video_success')
    else:
        form = TeaserVideoForm()

    return render(request, 'core/teaser_video.html', {'form': form})
