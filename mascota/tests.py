from unittest.mock import MagicMock

from django.test import TestCase, Client

from adopcion.models import Persona
from mascota.models import Mascota, Vacuna


# Create your tests here.
from mascota.views import MascotaList


class MascotaTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        persona1 = Persona.objects.create(nombre='fede', apellido='belve', edad='18', telefono='123', email='fede@gmail.com', domicilio='asdfsadf')
        person2 = MagicMock()
        vacuna1 = Vacuna.objects.create(nombre='Rabia')
        vacuna2 = Vacuna.objects.create(nombre='Otra')
        vacuna3 = Vacuna.objects.create(nombre='Otra Mas')
        self.mascota = Mascota.objects.create(codigo=1, nombre='pepe', sexo='Masc', edad_aproximada='28', fecha_rescate='2001-01-01', persona=persona1)
        self.mascota.vacuna.add(vacuna1, vacuna2, vacuna3)


    def test_mascota_vacunas(self):
        self.assertEqual(self.mascota.vacuna.count(),3)

#     def test_listMascota(self):
#         response = self.c.get('/mascota/listar/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_editMascota(self):
#          response = self.c.get('/mascota/editar/1')
#          self.assertEqual(response.status_code, 200)
#
#
#
# def setup_view(view, request, *args, **kwargs):
#     view.request = request
#     view.args = args
#     view.kawrgs = kwargs
#     return view
#
# def ViewTestCase(TestCase):
#     c = Client()
#     request = c.get('/mascota/listar/')
#     v = setup_view(MascotaList, request)
#
