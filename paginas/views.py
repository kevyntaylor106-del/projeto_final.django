from django.shortcuts import render

def home(request):

    return render(request, 'paginas/home.html', {'titulo': 'Página Inicial'})

def sobre(request):

    return render(request, 'paginas/sobre.html', {'titulo': 'Sobre Nós'})

def politica_privacidade(request):

    return render(request, 'paginas/politica_privacidade.html', {'titulo': 'Política de Privacidade'})

def termos_uso(request):

    return render(request, 'paginas/termos_uso.html', {'titulo': 'Termos de Uso'})

def contato(request):

    return render(request, 'paginas/contato.html', {'titulo': 'Contato'})

def ajuda(request):

    return render(request, 'paginas/ajuda.html', {'titulo': 'Ajuda'})

