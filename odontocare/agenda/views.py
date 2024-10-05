from django.shortcuts import render, redirect
from .forms import PacienteForm
from .models import Paciente

def home(request):
    pacientes = Paciente.objects.all()  # Lista todos os pacientes
    return render(request, 'home.html', {'pacientes': pacientes})

# View para cadastrar um novo paciente
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para a página de sucesso
    else:
        form = PacienteForm()

    return render(request, 'cadastrar_paciente.html', {'form': form})  # Certifique-se que o caminho do template está correto

def sucesso(request):
    return render(request, 'sucesso.html')




