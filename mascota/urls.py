from django.contrib import admin
from django.urls import path, include
from mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
#    path('home/', home, name='home'),
    path('nueva/', MascotaCreate.as_view(), name='mascota_crear'),
    path('listar/', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<pk>', MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<pk>', MascotaDelete.as_view(), name='mascota_eliminar'),
]
