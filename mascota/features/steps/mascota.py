from behave import given, when, then

from adopcion.models import Persona
from mascota.models import Mascota, Vacuna


@given ('an anonymous user')
def step_impl(context):
    persona = Persona.objects.create(nombre='fede', apellido='belve', edad='18', telefono='123',
                                      email='fede@gmail.com', domicilio='asdfsadf')
    persona.save()

    vacuna = Vacuna.objects.create(nombre='Rabia')
    vacuna.save()
    #mascota = Mascota.objects.create(codigo=1, nombre='pepe', sexo='Masc', edad_aproximada='28', fecha_rescate='2001-01-01', persona=persona)
    #mascota.vacuna.add(vacuna)
    #mascota.save()

@when('I submit a valid mascota form')
def step_impl(context):
    br = context.browser
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
    br = context.browser

    assert br.current_url.endwith('/mascota/listar/')
