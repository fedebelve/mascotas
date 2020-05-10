from django.contrib import admin

# Register your models here.
from adopcion.models import Persona
from mascota.models import Vacuna

admin.site.register(Persona)
admin.site.register(Vacuna)
