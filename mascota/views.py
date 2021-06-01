from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mascota.forms import MascotaForm, MascotaForm2
from mascota.models import Mascota, Mascotas


# def mascota_add(request):
#      if request.method == 'POST':
#         form = MascotaForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('mascota:mascota_listar')
#
#      else:
#         form = MascotaForm()
#      return render(request, 'mascota/mascotaForm.html', {'form': form})
#
#
# def mascota_list(request):
#     mascotas = Mascota.objects.all()
#     contexto = {'mascotas': mascotas}
#
#     return render(request, 'mascota/mascotaList.html', contexto)
#
#
# def mascota_edit(request, codigo_mascota):
#     mascota = Mascota.objects.get(codigo=codigo_mascota)
#     if request.method == 'GET':
#         form = MascotaForm(instance=mascota)
#     else:
#         form = MascotaForm(request.POST, instance=mascota)
#         if form.is_valid():
#             form.save()
#         return redirect('mascota:mascota_listar')
#
#     return render(request, 'mascota/mascotaForm.html', {'form': form})
#
#
# def mascota_delete(request, codigo_mascota):
#     mascota = Mascota.objects.get(codigo=codigo_mascota)
#     if request.method == 'POST':
#         mascota.delete()
#         return redirect('mascota:mascota_listar')
#
#     return render(request, 'mascota/mascotaDelete.html', {'mascota': mascota})



class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascotaList.html'


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascotaForm.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotasCreate(CreateView):
    model = Mascotas
    form_class = MascotaForm2
    template_name = 'mascota/mascotaForm.html'
    success_url = reverse_lazy('mascota:mascota_listar')



class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascotaForm.html'
    success_url = reverse_lazy('mascota:mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascotaDelete.html'
    success_url =  reverse_lazy('mascota:mascota_listar')