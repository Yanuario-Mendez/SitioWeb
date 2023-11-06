# urls.py
from django.contrib import admin
from django.urls import path
from registro import views as registro_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registro_views.home, name='home'),
    path('historial/', registro_views.historial_view, name='historial'),
    path('generar-cita/', registro_views.generar_cita_view, name='generar_cita'),
    path('cita-confirmada/<int:cita_id>/', registro_views.cita_confirmada_view, name='cita_confirmada'),
    path('medicos-servicios/', registro_views.medicos_servicios_view, name='medicos_servicios'),
    path('contacto/', registro_views.contacto_view, name='contacto'),
]


