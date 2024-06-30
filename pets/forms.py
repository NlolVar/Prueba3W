from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [ 'product_id','nombre_prod', 'precio', 'imagen']