

import br as br
from behave import given, when, then
from django.utils.datetime_safe import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from adopcion.models import Persona
from mascota.models import Mascota, Vacuna
import time


@given ('an anonymous user')
def step_impl(context):
    persona = Persona.objects.create(nombre='fede', apellido='belve', edad='18', telefono='123',
                                      email='fede@gmail.com', domicilio='asdfsadf')
    persona.save()

    vacuna = Vacuna.objects.create(nombre='Rabia')
    vacuna.save()


@when('I submit a valid mascota form')
def step_impl(context):
    br = webdriver.PhantomJS()
    br.get(context.base_url + '/mascota/nuevo/')

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('codigo').send_keys('1')
    br.find_element_by_name('nombre').send_keys('algo')
    br.find_element_by_name('edad_aproximada').send_keys('28')
    br.find_element_by_name('fecha_rescate').send_keys('01-01-2001')
    br.find_element_by_name('sexo').send_keys('masc')
    br.find_element_by_name('persona').send_keys('1')
    br.find_element_by_name('vacuna').send_keys('1')
    br.find_element_by_name('guardar').click()



@then('I am redirect to the list page')
def step_impl(context):
    br = webdriver.PhantomJS()
    time.sleep(20)
    print(br.current_url)

    assert br.current_url == (context.base_url + '/mascota/listar')

    #assert br.current_url. ('/mascota/nuevo/')
