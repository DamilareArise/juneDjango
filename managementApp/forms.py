from django import forms
from .models import StockLog


class StockLogForm(forms.ModelForm):
    
    class Meta:
        model = StockLog
        fields = [
            'quantity',
            'type'
        ]