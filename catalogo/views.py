from django.shortcuts import render
from .models import Prenda, Colores, Marcas,Tallas
from django.views import generic

# Create your views here.
def index(request):
    return render(request,'index.html')

def sidebar(request):
    return render(request,'sidebar.html')

def about(request):
    return render(request,'about.html')

def contacto(request):
    return render(request,'contact.html')

class PrendaListView(generic.ListView):
    model= Prenda

