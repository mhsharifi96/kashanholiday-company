from django.contrib import admin
from .models import Tour, TourVariation, TourImage, Category
from restaurants.models import RestaurantLocation
# Register your models here.
# admin.site.register(Tour)
admin.site.register(TourVariation)
admin.site.register(TourImage)
admin.site.register(Category)
# class ProductImagesInline(admin.TabularInline):
#     model = Tour

class Product2ImagesInline(admin.TabularInline):
    model = RestaurantLocation

class ProductsAdmin(admin.ModelAdmin):
    inlines = [
        Product2ImagesInline
    ]

admin.site.register(Tour, ProductsAdmin)
