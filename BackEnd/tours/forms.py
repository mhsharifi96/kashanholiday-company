from .models import TourVariation
from django import forms

class TourVariationInventoryForm(forms.ModelForm):
    class Meta:
        model = TourVariation
        fields = [
            "price",
            "sale_price",
            "inventory"
        ]