from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    dpi = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    razon_visita = models.TextField()
    receta_medica = models.TextField()
    numero_telefonico = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    numero_colegiado = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=50)
    diagnostico = models.TextField()

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    nombre = models.CharField(max_length=100, default='')  # Valor predeterminado para nombre
    telefono = models.CharField(max_length=20, default='')  # Valor predeterminado para telefono
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField(default=timezone.now)
    razon_visita = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M')} - {self.medico.nombre}"