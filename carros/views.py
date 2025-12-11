from django.shortcuts import render

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
