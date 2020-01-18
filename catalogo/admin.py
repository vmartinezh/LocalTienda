from django.contrib import admin

# Register your models here.

from . models import Prenda, Colores, Marcas, Tallas

admin.site.register(Prenda)
admin.site.register(Colores)
admin.site.register(Marcas)
admin.site.register(Tallas)

