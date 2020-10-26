from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Форма таблицы Product.
    """
    class Meta:
        model = Order
        fields = ('price_order', 'contractor', 'description',)
