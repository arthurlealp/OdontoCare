from django import forms
from .models import Paciente

# Formulário para cadastrar pacientes
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'contato']
