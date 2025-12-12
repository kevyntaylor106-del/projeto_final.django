from django.urls import path
from . import views

app_name = 'paginas' 

urlpatterns = [
    path('', views.home, name='home'), 
    path('sobre/', views.sobre, name='sobre'),
    path('politica-privacidade/', views.politica_privacidade, name='politica_privacidade'), 
]