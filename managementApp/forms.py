from django import forms
from .models import StockLog


class StockLogForm(forms.ModelForm):
    
    class Meta:
        model = StockLog
        fields = [
            'quantity',
            'type'
        ]
        
        widgets  = {
            "quantity": forms.NumberInput(attrs={"class": "form-control mb-2", "placeholder":"Quantity"}),
            "type": forms.Select(attrs={"class": "form-control mb-2"})
        }