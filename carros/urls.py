# from django.urls import path, include
# from django.contrib import admin


# urlpatterns = [
#     path('/', include('carros.urls')),
#     path('admin/', admin.site.urls),
# ]#

from django.shortcuts import render, get_object_or_404
from .models import Carro # Use o nome da classe em maiúsculo

def lista_carros(request):
    # Alterado o nome da variável para não conflitar com a classe
    lista_de_carros = Carro.objects.all()
    return render(request, 'carros/lista_carros.html', {'carros': lista_de_carros})

def detalhe_carro(request, carro_id):
    # Se o ID não existir, o Django exibe uma página 404 amigável
    carro = get_object_or_404(Carro, id=carro_id)
    return render(request, 'carros/detalhe_carro.html', {'carro': carro})