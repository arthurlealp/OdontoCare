from django.urls import path
from . import views

# Definir as URLs do app agenda
urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('excluir_paciente/<int:paciente_id>/', views.excluir_paciente, name='excluir_paciente'),
    path('sucesso/', views.sucesso, name='sucesso'),
]