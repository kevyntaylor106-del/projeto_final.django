from django.shortcuts import render
from .models import carros

def lista_carros(request):
    carros = carros.objects.all()
    return render(request, 'carros/lista_carros.html', {'carros': carros})  