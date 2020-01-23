from django.shortcuts import render
from .models import Prenda, Colores, Marcas,Tallas
from django.views import generic

# Create your views here.
def index(request):

    num_prenda= Prenda.objects.all().count()
    num_colores= Colores.objects.all().count()


    return render(
        request,
        'index.html',
        context={'num_prenda': num_prenda, 'num_colores': num_colores},
    )

def sidebar(request):
    return render(request,'sidebar.html')

def about(request):
    return render(request,'about.html')

def contacto(request):
    return render(request,'contact.html')

class PrendaListView(generic.ListView):
    model= Prenda

