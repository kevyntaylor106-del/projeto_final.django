from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import path, include
# from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator   



from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.urls import reverse_lazy

from .models import (
    Categoria,
    Produto,
    Cliente,
)

from django.forms import (
    CategoriaForm,
    ProdutoForm,
    ClienteForm,
)

# Create your views here.



class CategoriaListView(ListView):
    model = Categoria
    template_name = "produtos/categorias/categoria_list_simples.html"
    context_object_name = "categorias"

    class CategoriaDetailView(DetailView):
        model = Categoria
        template_name = "produtos/categorias/categoria_detail.html"
        context_object_name = "categoria"

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "produtos/categorias/categoria_form.html"
    success_url = reverse_lazy("categoria-list")

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "produtos/categorias/categoria_form.html"
    success_url = reverse_lazy("categoria-list")

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):  
    model = Categoria
    template_name = "produtos/categorias/categoria_confirm_delete.html"
    success_url = reverse_lazy("categoria-list")    

class ProdutoListView(ListView):
    model = Produto
    template_name = "produtos/produtos/produto_list_simples.html"
    context_object_name = "produtos"

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produtos/produto_form.html"
    success_url = reverse_lazy("produto-list")  

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produtos/produto_form.html"
    success_url = reverse_lazy("produto-list")

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):  
    model = Produto
    template_name = "produtos/produtos/produto_confirm_delete.html"
    success_url = reverse_lazy("produto-list")

class ClienteListView(ListView):
    model = Cliente
    template_name = "produtos/clientes/cliente_list_simples.html"
    context_object_name = "clientes"

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "produtos/clientes/cliente_form.html"
    success_url = reverse_lazy("cliente-list")

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "produtos/clientes/cliente_form.html"
    success_url = reverse_lazy("cliente-list")

class ClienteDeleteView(LoginRequiredMixin, DeleteView):  
    model = Cliente
    template_name = "produtos/clientes/cliente_confirm_delete.html"
    success_url = reverse_lazy("cliente-list")

    class ClienteUserAccessMixin(UserPassesTestMixin):
        def test_func(self):
            cliente = self.get_object()
            return cliente.usuario == self.request.user
        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    class djangohttpresponseredirect(HttpResponseRedirect):
        pass

        def get_success_url(self):
            return reverse("cliente-list")
        
        class djangourlsreverselazy(reverse_lazy):
            pass

        class path(path):
            pass

        class insclude(include):
            pass