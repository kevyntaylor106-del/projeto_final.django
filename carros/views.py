# from django.shortcuts import render
# from .models import carros

# def lista_carros(request):
#     carros = carros.objects.all()
#     return render(request, 'carros/lista_carros.html', {'carros': carros})

# def detalhe_carro(request, carro_id):
#     carro = carros.objects.get(id=carro_id)
#     return render(request, 'carros/detalhe_carro.html', {'carro': carro})   

# def criar_pedido(request, carro_id):
#     carro = carros.objects.get(id=carro_id)
#     # Lógica para criar um pedido para o carro
#     return render(request, 'carros/pedido_criado.html', {'carro': carro})

# from django.test import TestCase
# from django.contrib.auth.models import User

# class CarroModelTest(TestCase):
#     def setUp(self):
#         self.carro = Carro.objects.create(
#             nome="Fusca",
#             modelo="Volkswagen",
#             ano_modelo=1970,
#             km_rodados=150000.0,
#             cor="Azul",
#             pecas_substituidas="Pneus, Freios",
#             transmissao='M',
#             preco=Decimal('15000.00'),
#             descricao="Um clássico carro brasileiro."
#         )

#     def test_carro_creation(self):
#         self.assertEqual(self.carro.nome, "Fusca")
#         self.assertEqual(str(self.carro), "Fusca Volkswagen (1970)")

# class PerfilModelTest(TestCase):    
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.perfil = Perfil.objects.create(
#             usuario=self.user,
#             telefone="123456789",
#             endereco="Rua Teste, 123"
#         )

#     def test_perfil_creation(self):
#         self.assertEqual(self.perfil.usuario.username, 'testuser')
#         self.assertEqual(str(self.perfil), "Perfil: testuser")

# class PedidoModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='cliente', password='12345')
#         self.pedido = Pedido.objects.create(
#             cliente=self.user
#         )

from django.urls import reverse
from .models import Carro

class CarroViewTest(TestCase):
    def setUp(self):
        # Criamos um carro para testar a listagem e o detalhe
        self.carro = Carro.objects.create(
            nome="Fusca",
            modelo="Volkswagen",
            ano_modelo=1970,
            preco=15000.00,
            transmissao='M'
        )

    def test_lista_carros_view(self):
        """Testa se a lista de carros retorna status 200 e o contexto correto"""
        response = self.client.get(reverse('lista_carros')) # Ajuste o nome da URL se necessário
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.carro, response.context['carros'])
        self.assertContains(response, "Fusca")

    def test_detalhe_carro_view(self):
        """Testa a página de detalhes de um carro específico"""
        response = self.client.get(reverse('detalhe_carro', args=[self.carro.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['carro'].nome, "Fusca")