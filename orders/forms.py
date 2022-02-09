
from django import forms

from .models import Order,OrderProduct

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields= '__all__'
class OrderProductModelForm(forms.ModelForm):
    class Meta:
        model= OrderProduct
        fields='__all__'