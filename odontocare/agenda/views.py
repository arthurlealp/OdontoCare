from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm
from .models import Paciente
from django.http import JsonResponse


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
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, id=paciente_id)
        paciente.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)




