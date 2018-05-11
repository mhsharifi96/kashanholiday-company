from django.contrib import admin
from .models import Tour, TourVariation, TourImage, Category
# Register your models here.
admin.site.register(Tour)
admin.site.register(TourVariation)
admin.site.register(TourImage)
admin.site.register(Category)