from behave import given, when, then
from behave.textutil import text
from selenium.webdriver.support.ui import Select
import  logging
from adopcion.models import Persona
from mascota.models import Mascotas, Vacuna


@given('una persona y una vacuna')
def step_impl(context):
    persona = Persona.objects.create(nombre='fede', apellido='belve', edad='18', telefono='123',
                                     email='fede@gmail.com', domicilio='asdfsadf')
    persona.save()

    vacuna = Vacuna.objects.create(nombre='Rabia')
    vacuna.save()


@when('I submit a valid mascota form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/mascota/nueva/')

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('codigo').send_keys('1111')
    br.find_element_by_name('nombre').send_keys('algo')
    br.find_element_by_name('edad_aproximada').send_keys('28')
    br.find_element_by_name('fecha_rescate').send_keys('2001-01-01')
    br.find_element_by_name('sexo').send_keys('masc')
    persona = Select(br.find_element_by_name('persona'))
    persona.select_by_value('1')
    br.find_element_by_name('vacuna').click()
    br.find_element_by_name('guardar').click()


@then('I am redirect to the list page')
def step_impl(context):
    br = context.browser
    codigo = br.find_element_by_name('codigo').text
    assert '1111' in codigo
    assert '/mascota/listar/' in br.current_url





@when('I submit an invalid mascota form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/mascota/nueva/')

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('nombre').send_keys('algo')
    br.find_element_by_name('edad_aproximada').send_keys('28')
    br.find_element_by_name('fecha_rescate').send_keys('2001-01-01')
    br.find_element_by_name('sexo').send_keys('masc')
    persona = Select(br.find_element_by_name('persona'))
    persona.select_by_value('1')
    br.find_element_by_name('vacuna').click()
    br.find_element_by_name('guardar').click()


@then('I am redirect to the same page')
def step_impl(context):
    br = context.browser
    assert '/mascota/nueva/' in br.current_url
