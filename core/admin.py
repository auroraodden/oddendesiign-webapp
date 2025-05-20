from django.contrib import admin

# Register your models here.
from .models import Customer, Product, Order, Review, GalleryImage, UploadedFile
from .models import TeaserProduct, TeaserVideo, TeaserVideoFile

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'contact_email', 'contact_phone', 'address') # Viser nevnt
    search_fields = ('group_name', 'contact_email') # Kan søke på navn eller e-post

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'is_outlet') # Viser nevnt
    list_filter = ('is_available', 'is_outlet') # Filtrerer på tilgjengelighet
    search_fields = ('title',) # Kan søke på tittel

class UploadedFileInline(admin.TabularInline):
    model = UploadedFile
    extra = 1
    readonly_fields = ('file',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'created_at', 'is_completed') # Viser nevnt
    list_filter = ('is_completed', 'created_at') # Filtrerer/status på fullført/ikke fullført og dato
    search_fields = ('customer__group_name', 'product__title') # Kan søke nevnt
    inlines = [UploadedFileInline] # Viser opplastede filer i bestillingen

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'rating', 'created_at', 'is_approved') # Viser nevnt
    list_filter = ('rating', 'is_approved', 'created_at') # Filtrerer på vurdering
    search_fields = ('customer__group_name', 'text') # Kan søke nevnt

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at') # Viser nevnt
    search_fields = ('title',) # Kan søke på tittel

@admin.register(TeaserProduct)
class TeaserProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available')
    search_fields = ('title',)
    list_filter = ('is_available',)

class TeaserVideoFileInline(admin.TabularInline):
    model = TeaserVideoFile
    extra = 1

@admin.register(TeaserVideo)
class TeaserVideoAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'product', 'full_name', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('group_name', 'full_name', 'email', 'product')
    readonly_fields = ('created_at',)
    inlines = [TeaserVideoFileInline]
