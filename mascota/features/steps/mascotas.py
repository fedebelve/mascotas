from behave import given, when, then

from adopcion.models import Persona
from mascota.models import Mascotas, Vacuna



@when('I submit a valid mascota form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/mascota/nueva/')

    #assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('codigo').send_keys('1')
    br.find_element_by_name('nombre').send_keys('algo')
    br.find_element_by_name('edad_aproximada').send_keys('28')
    br.find_element_by_name('fecha_rescate').send_keys('01-01-2001')
    br.find_element_by_name('sexo').send_keys('masc')
    br.find_element_by_name('guardar').click()


@then('I am redirect to the list page')
def step_impl(context):
    br = context.browser
    print(br.current_url)
    #assert br.current_url.endwith('/mascota/listar/')
