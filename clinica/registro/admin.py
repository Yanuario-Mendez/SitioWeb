from django.contrib import admin
from .models import Paciente, Medico, Cita

class CitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'medico', 'fecha_hora', 'razon_visita')
    search_fields = ['nombre']  # Permite buscar por nombre

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_colegiado', 'especialidad')
    search_fields = ['numero_colegiado']  # Permite la búsqueda por número de colegiado

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dpi', 'fecha_nacimiento', 'direccion', 'numero_telefonico')
    search_fields = ['dpi']  # Permite la búsqueda por DPI

# Registra modelos usando las clases ModelAdmin
admin.site.register(Cita, CitaAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)

