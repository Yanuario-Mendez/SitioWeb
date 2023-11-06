# views.py
from django.shortcuts import render, redirect
from .models import Medico, Cita
from .forms import CitaForm

# La vista actual para la página de inicio
def home(request):
    return render(request, 'index.html')

# Vista para la página de historial
def historial_view(request):
    return render(request, 'historial.html')

# Vista para la página de generar cita
def generar_cita_view(request):
    especialidades = Medico.objects.values_list('especialidad', flat=True).distinct()
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save()
            return redirect('cita_confirmada', cita_id=cita.id)
    else:
        form = CitaForm()
    return render(request, 'generar_cita.html', {'form': form, 'especialidades': especialidades})

# vista para confirmar la cita
def cita_confirmada_view(request, cita_id):
    cita = Cita.objects.get(id=cita_id)
    return render(request, 'cita_confirmada.html', {'cita': cita})

# Vista para la página de médicos/servicios
def medicos_servicios_view(request):
    medicos = Medico.objects.all()  # Recupera todos los médicos de la base de datos
    return render(request, 'medicos_servicios.html', {'medicos': medicos})


# Vista para la página de contacto
def contacto_view(request):
    return render(request, 'contacto.html')




