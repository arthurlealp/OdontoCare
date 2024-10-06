from django.urls import path
from . import views

# Definir as URLs do app agenda
urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('paciente/excluir/<int:paciente_id>/', views.excluir_paciente, name='excluir_paciente'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('consulta/editar/<int:consulta_id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/', views.lista_consultas, name='lista_consultas'),  # URL para lista de consultas
    path('consulta/cadastrar/', views.cadastrar_consulta, name='cadastrar_consulta'),
    path('consulta/excluir/<int:consulta_id>/', views.excluir_consulta, name='excluir_consulta'),
]