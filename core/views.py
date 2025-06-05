from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import OutletOrder
from .forms import OutletOrderForm
from django.shortcuts import get_object_or_404
from .models import FAQ

from .forms import OrderForm, TeaserVideoForm
from .models import (
    Customer, GalleryImage, Product, Review,
    UploadedFile, TeaserVideoFile
)
from .forms import ContactMessageForm

# ----------------------------- Startside -----------------------------

def index(request):
    outlet_products = Product.objects.filter(is_outlet=True, is_available=True)[:3]
    faqs = FAQ.objects.all().order_by('display_order')[:6]
    reviews = Review.objects.filter(is_approved=True).order_by('-created_at')[:5]
    contact_form = ContactMessageForm()
    return render(request, 'core/index.html', {'products': outlet_products, 'faqs': faqs, 'reviews': reviews, 'form': contact_form})
    
# ----------------------------- Galleri -----------------------------

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})

# ----------------------------- Outlet -----------------------------

def outlet(request):
    products = Product.objects.filter(is_available=True, is_outlet=True)
    return render(request, 'core/outlet.html', {'products': products})

# ----------------------------- Kundeomtaler -----------------------------

def reviews_page(request):
    reviews = Review.objects.filter(is_approved=True)
    return render(request, 'core/reviews.html', {'reviews': reviews})

# ----------------------------- LOGO-BESTILLING -----------------------------

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)

            customer = Customer.objects.create(
                group_name=order.group_name,
                contact_email=order.email,
                contact_phone=order.phone,
                address=order.address,
            )
            order.customer = customer

            if order.product:
                order.total_price = order.product.price

            order.save()

            files = request.FILES.getlist('uploaded_files')
            for f in files:
                UploadedFile.objects.create(order=order, file=f)

            # ✉️ HTML-e-post med tekstfallback og blindkopi
            subject = 'Bekreftelse på bestilling hos Oddendesiign 🎨'
            context = {'order': order}
            html_content = render_to_string('core/emails/order_confirmation.html', context)
            text_content = f"Takk for bestillingen, {order.full_name}!"

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[order.email],
                bcc=['oddendesign@gmail.com']
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return render(request, 'core/order_success.html')
    else:
        form = OrderForm()

    return render(request, 'core/order.html', {'form': form})

# ----------------------------- TEASERVIDEO-BESTILLING -----------------------------

def teaser_video_view(request):
    if request.method == 'POST':
        form = TeaserVideoForm(request.POST, request.FILES)
        if form.is_valid():
            teaser = form.save(commit=False)

            if teaser.product:
                teaser.total_price = teaser.product.price
            
            teaser.save()

            files = request.FILES.getlist('files')
            for f in files:
                TeaserVideoFile.objects.create(teaser_video=teaser, file=f)

            # ✉️ HTML-e-post med tekstfallback og blindkopi
            subject = f"Bekreftelse på teaservideo-bestilling - {teaser.group_name}"
            context = {'teaser': teaser}
            html_content = render_to_string('core/emails/teaser_confirmation_email.html', context)
            text_content = f"Takk for bestillingen, {teaser.full_name}!"

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[teaser.email],
                bcc=['oddendesign@gmail.com']
            )
            email.attach_alternative(html_content, "text/html")

            for f in teaser.files.all():
                if f.file:
                    email.attach_file(f.file.path)
            
            email.send()

            return render(request, 'core/teaser_video_success.html')
    else:
        form = TeaserVideoForm()

    return render(request, 'core/teaser_video.html', {'form': form})

# ----------------------------- FERDIG LOGO-BESTILLING -----------------------------

def outlet_order_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_available=True, is_outlet=True)

    if request.method == 'POST':
        form = OutletOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.total_price = product.price
            order.save()

            product.is_available = False # Gjør produktet utilgjengelig etter bestilling
            product.save()

            subject = f"Kjøp av ferdig logo - {product.title}"
            context = {'order': order}
            html_content = render_to_string('core/emails/order_confirmation.html', context)
            text_content = f"Takk for kjøpet, {order.full_name}!"

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[order.email],
                bcc=['oddendesign@gmail.com']
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return render(request, 'core/order_success.html')
    else:
        form = OutletOrderForm()

    return render(request, 'core/outlet_order.html', {'form': form, 'product': product})

# ----------------------------- KONTAKTSKJEMA -----------------------------

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            subject = f"Oddendesiign: {contact.subject}"
            context = {'contact': contact}
            html_content = render_to_string('core/emails/contact_confirmation.html', context)
            text_content = f"Takk for at du kontaktet oss, {contact.full_name}!\n\nVi har mottatt meldingen din og svarer så snart vi kan."

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[contact.email],
                bcc=['oddendesign@gmail.com']  
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return redirect('contact_success')
    else:
        form = ContactMessageForm()

    return render(request, 'core/contact.html', {'form': form})

# ----------------------------- FAQ -----------------------------

def faq_view(request):
    faqs = FAQ.objects.all().order_by('display_order')

    return render(request, 'core/faq.html', {'faqs': faqs})

# ----------------------------- OM OSS -----------------------------

def about_view(request):
    return render(request, 'core/about.html')

# ----------------------------- BETINGELSER OG VILKÅR -----------------------------

def terms_view(request):
    return render(request, 'core/terms.html')
