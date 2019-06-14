from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category',  'size', 'code', 'price', 'quantity', 'packed', 'seller', 'date')

class LivrOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('delivered','city')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('store_name',  'order_date',   'order_number',   'sku',   'product',   'client_name',   'phone',   'address', 'city', 'price', 'packed', 'confirmed' , 'sent'   , 'delivered')


class DelEditOrder(OrderForm):
    class Meta:
        model = Order
        fields = ('delivered',)