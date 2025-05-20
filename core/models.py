from django.db import models

# Create your models here.
class Customer(models.Model):
    group_name = models.CharField(max_length=255)
    contact_email = models.EmailField() # Obligatorisk
    contact_phone =models.CharField(max_length=20) # Obligatorisk
    address = models.TextField() # Obligatorisk

    def __str__(self):
        return self.group_name 

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    custom_description = models.TextField(blank=True) # Beskrivelse av produktet
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
    # Feltene som trengs til skjemaet
    group_name = models.CharField(max_length=255)
    concept_description = models.TextField()
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()
    agree_to_terms = models.BooleanField(default=False)
    color_1 = models.CharField(max_length=7, blank=True)
    color_2 = models.CharField(max_length=7, blank=True)
    color_3 = models.CharField(max_length=7, blank=True)
    color_4 = models.CharField(max_length=7, blank=True)
    color_5 = models.CharField(max_length=7, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class UploadedFile(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='uploaded_files')
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"Order #{self.id} - {self.customer.group_name}"

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False) # Godkjenning av anmeldelse

    def __str__(self):
        return f"Review by {self.customer}"

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class TeaserProduct(models.Model): # Teaservideo produkter
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class TeaserVideo(models.Model):
    product = models.ForeignKey(TeaserProduct, on_delete=models.SET_NULL, null=True)
    group_name = models.CharField(max_length=255)
    concept_description = models.TextField()
    video_style = models.CharField(max_length=100)
    music_preference = models.CharField(max_length=100, blank=True)

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()

    agree_to_terms = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_name} – {self.product}"

class TeaserVideoFile(models.Model): # Flerfil opplasting knyttet til teaservideo-bestilling
    teaser_video = models.ForeignKey(TeaserVideo, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.file.name