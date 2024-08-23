from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('adicionar/', views.adicionar_nota, name='adicionar_nota'),
    path('atualizar/<int:pk>/', views.atualizar_nota, name='atualizar_nota'),
    path('remover/<int:pk>/', views.remover_nota, name='remover_nota'),
]

