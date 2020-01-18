from django.shortcuts import render
from .models import Prenda, Colores, Marcas,Tallas

# Create your views here.
def index(request):

    num_prenda= Prenda.objects.all().count()
    num_colores= Colores.objects.all().count()


    return render(
        request,
        'index.html',
        context={'num_prenda': num_prenda, 'num_colores': num_colores},
    )