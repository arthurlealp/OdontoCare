from django import forms
from .models import Paciente
from .models import Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'cpf', 'telefone']
        
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'data', 'hora', 'motivo', 'status', 'data_que_veio']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'data', 'hora', 'motivo', 'status']