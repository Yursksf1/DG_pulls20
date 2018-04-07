from django.contrib import admin

# Register your models here.
from .models import Certificados, Estudiates, Solicitudes

admin.site.register(Certificados)
admin.site.register(Estudiates)
admin.site.register(Solicitudes)

