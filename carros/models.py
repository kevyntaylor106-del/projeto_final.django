from django.db import models
from django.contrib.auth.models import User

# PERFIL DO CLIENTE
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return f"Perfil: {self.usuario.username}"

# CLASSE CARROS (O PRODUTO)
class Carro(models.Model):
    TRANSMISSAO_CHOICES = [('M', 'Manual'), ('A', 'Automático')]
    
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_modelo = models.PositiveIntegerField()
    km_rodados = models.FloatField()
    cor = models.CharField(max_length=50)
    pecas_substituidas = models.TextField(blank=True, help_text="Ex: Pneus, Freios...")
    transmissao = models.CharField(max_length=1, choices=TRANSMISSAO_CHOICES)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.nome} {self.modelo} ({self.ano_modelo})"

# PEDIDO DE COMPRA
class Pedido(models.Model):
    STATUS_CHOICES = [('P', 'Pendente'), ('F', 'Finalizado'), ('C', 'Cancelado')]
    
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"

# ITENS DO PEDIDO (O CARRO ESPECÍFICO SENDO COMPRADO)
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.PROTECT) # PROTECT impede apagar carro com venda ativa
    quantidade = models.PositiveIntegerField(default=1)
    preco_venda = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.carro.nome} no Pedido {self.pedido.id}"
    
# SINAL PARA CRIAR PERFIL AUTOMATICAMENTE AO CRIAR USUÁRIO

from django.db.models.signals import post_save
from django.dispatch import receiver