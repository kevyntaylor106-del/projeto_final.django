from django.test import TestCase
from .models import Carro, Perfil, Pedido, ItemPedido
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal

class CarroModelTest(TestCase):
    def setUp(self):
        self.carro = Carro.objects.create(
            nome="Fusca",
            modelo="Volkswagen",
            ano_modelo=1970,
            km_rodados=150000.0,
            cor="Azul",
            pecas_substituidas="Pneus, Freios",
            transmissao='M',
            preco=Decimal('15000.00'),
            descricao="Um clássico carro brasileiro."
        )

    def test_carro_creation(self):
        self.assertEqual(self.carro.nome, "Fusca")
        self.assertEqual(str(self.carro), "Fusca Volkswagen (1970)")


class PerfilModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.perfil = Perfil.objects.create(
            usuario=self.user,
            telefone="123456789",
            endereco="Rua Teste, 123"
        )

    def test_perfil_creation(self):
        self.assertEqual(self.perfil.usuario.username, 'testuser')
        self.assertEqual(str(self.perfil), "Perfil: testuser")

class PedidoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cliente', password='12345')
        self.pedido = Pedido.objects.create(
            cliente=self.user
        )

    def test_pedido_creation(self):
        self.assertEqual(self.pedido.cliente.username, 'cliente')
        self.assertEqual(str(self.pedido), f"Pedido {self.pedido.id} - {self.user.username}")

class ItemPedidoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cliente2', password='12345')
        self.carro = Carro.objects.create(      
            nome="Civic",
            modelo="Honda",
            ano_modelo=2020,
            km_rodados=10000.0,
            cor="Preto",
            pecas_substituidas="",
            transmissao='A',
            preco=Decimal('80000.00'),
            descricao="Um carro moderno e eficiente."
        )

        self.pedido = Pedido.objects.create(
            cliente=self.user   
        )

        self.item_pedido = ItemPedido.objects.create(
            pedido=self.pedido,     
            carro=self.carro,
            quantidade=1,
            preco_venda=Decimal('75000.00')
        )

    def test_item_pedido_creation(self):
        self.assertEqual(self.item_pedido.pedido.id, self.pedido.id)
        self.assertEqual(self.item_pedido.carro.nome, "Civic")
        self.assertEqual(str(self.item_pedido), f"Civic no Pedido {self.pedido.id}")

        reverse_url = reverse('detalhe_carro', args=[self.carro.id])
        response = self.client.get(reverse_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Civic")

        
# Create your tests here.
