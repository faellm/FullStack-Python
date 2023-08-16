from django.urls import path
from . import views

urlpatterns = [
    path('painel/', views.painel_controle, name='painel_controle'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
]
