from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Prenda(models.Model):

    id_prenda = models.UUIDField(default=uuid.uuid4)
    nombre = models.CharField(max_length=50, primary_key=True)
    descripcion = models.TextField(max_length=200)
    precio = models.PositiveIntegerField()
    cantidad = models.SmallIntegerField()
    id_marca = models.ForeignKey(
        'Marcas', on_delete=models.CASCADE)
    id_color = models.ForeignKey(
        'Colores', on_delete=models.CASCADE)
    id_talla = models.ForeignKey(
        'Tallas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("prenda-details", args=[str(self.nombre)])    

class Marcas(models.Model):

    id_marca = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.id_marca
    



class Colores(models.Model):

    id_color = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.id_color
    



class Tallas(models.Model):

    id_talla = models.CharField(max_length=3, primary_key=True)
    descripcion = models.CharField(max_length=3)

    def __str__(self):
        return self.id_talla
    