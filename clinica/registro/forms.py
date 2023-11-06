from django import forms
from .models import Paciente, Medico, Cita

# Formulario para Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

# Formulario para Medico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

# Formulario para Cita
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre', 'telefono', 'medico', 'fecha_hora', 'razon_visita']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }