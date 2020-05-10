from django.contrib import admin
from django.urls import path, include
from adopcion.views import SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<pk>', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<pk>', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]
