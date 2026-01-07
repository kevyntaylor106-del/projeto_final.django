
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Carro, Perfil, Pedido, ItemPedido  # Certifique-se de que os nomes batem com models.py

# 1. Registro customizado para o modelo User (opcional)
# Primeiro desregistramos o padrão para registrar o nosso
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# 2. Registro do modelo Carro       
@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'modelo', 'ano', 'preco')
    search_fields = ('nome', 'modelo')
    list_filter = ('ano',)
    ordering = ('-ano',)

# 3. Registro do modelo Perfil
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):    
    list_display = ('usuario', 'telefone')
    search_fields = ('usuario__username', 'telefone')
    ordering = ('usuario__username',)

# 4. Registro do modelo Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_pedido', 'status')
    search_fields = ('cliente__username', 'status')
    ordering = ('-data_pedido',)

# 5. Registro do modelo ItemPedido
@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):    
    list_display = ('pedido', 'carro', 'quantidade', 'preco_venda')
    search_fields = ('pedido__id', 'carro__nome')
    ordering = ('pedido__id',)