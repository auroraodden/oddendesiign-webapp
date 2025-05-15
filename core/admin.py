from django.contrib import admin

# Register your models here.
from .models import Customer, Product, Order, Review, GalleryImage

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'contact_email', 'contact_phone', 'address') # Viser nevnt
    search_fields = ('group_name', 'contact_email') # Kan søke på navn eller e-post

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available') # Viser nevnt
    list_filter = ('is_available',) # Filtrerer på tilgjengelighet
    search_fields = ('title',) # Kan søke på tittel

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'created_at', 'is_completed') # Viser nevnt
    list_filter = ('is_completed', 'created_at') # Filtrerer/status på fullført/ikke fullført og dato
    search_fields = ('customer__group_name', 'product__title') # Kan søke nevnt

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'rating', 'created_at') # Viser nevnt
    list_filter = ('rating',) # Filtrerer på vurdering
    search_fields = ('customer__group_name', 'text') # Kan søke nevnt

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at') # Viser nevnt
    search_fields = ('title',) # Kan søke på tittel