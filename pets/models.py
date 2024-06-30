from django.db import models

# Create your models here.

class Producto(models.Model):
    product_id = models.CharField(primary_key=True, max_length=10)
    nombre_prod = models.CharField(max_length=999)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField()