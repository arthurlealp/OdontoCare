from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm
from .models import Paciente
from django.http import JsonResponse
from .models import Consulta
from .forms import ConsultaForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    pacientes = Paciente.objects.all()  # Lista todos os pacientes
    return render(request, 'home.html', {'pacientes': pacientes})

# View para cadastrar um novo paciente
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do paciente
            return redirect('sucesso')  # Redireciona para a página de sucesso
        else:
            # Se o formulário não for válido, renderiza o formulário com erros
            return render(request, 'cadastrar_paciente.html', {'form': form})
    else:
        # Se for uma requisição GET, exibe o formulário vazio
        form = PacienteForm()
        return render(request, 'cadastrar_paciente.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')

def home(request):
    pacientes = Paciente.objects.all()
    return render(request, 'home.html', {'pacientes': pacientes})

def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'POST':
        paciente.delete()
        return JsonResponse({'success': True})  # Retorna sucesso em formato JSON

    return JsonResponse({'success': False})  # Se não for POST, retorna erro

def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)  # Obtém a consulta pelo ID ou retorna 404 se não existir
    pacientes = Paciente.objects.all()  # Obtém todos os pacientes

    if request.method == 'POST':
        consulta.paciente_id = request.POST.get('paciente')
        consulta.data = request.POST.get('data')
        consulta.hora = request.POST.get('hora')
        consulta.motivo = request.POST.get('motivo')
        consulta.status = request.POST.get('status')
        consulta.save()  # Salva as alterações da consulta
        return redirect('lista_consultas')  # Redireciona após salvar as alterações

    return render(request, 'editar_consulta.html', {'consulta': consulta, 'pacientes': pacientes})

def lista_consultas(request):
    consultas = Consulta.objects.all()  # Busca todas as consultas do banco de dados
    return render(request, 'lista_consultas.html', {'consultas': consultas})

def cadastrar_consulta(request):
    pacientes = Paciente.objects.all()  # Obtém todos os pacientes

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        motivo = request.POST.get('motivo')
        status = request.POST.get('status')

        # Validação e processamento dos dados
        paciente = Paciente.objects.get(id=paciente_id)
        consulta = Consulta(
            paciente=paciente,
            data=data,
            hora=hora,
            motivo=motivo,
            status=status
        )
        consulta.save()  # Salva a nova consulta no banco de dados
        return redirect('lista_consultas')  # Redireciona para a lista de consultas após salvar

    return render(request, 'cadastrar_consulta.html', {'pacientes': pacientes})

@csrf_exempt
def excluir_consulta(request, consulta_id):
    if request.method == 'POST':
        consulta = get_object_or_404(Consulta, id=consulta_id)
        consulta.delete()
        return JsonResponse({'status': 'Consulta excluída com sucesso'})



