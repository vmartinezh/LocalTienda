from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('tienda', views.sidebar, name='sidebar'),
    path('about', views.about, name='about'),
    path('contact', views.contacto, name='contact'),

]
