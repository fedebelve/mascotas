from django import forms

from mascota.models import Mascota


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'codigo',
            'nombre',
            'edad_aproximada',
            'fecha_rescate',
            'sexo',
            'persona',
            'vacuna',
            'tipo_mascota'
        ]
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'edad_aproximada': 'Edad Aproximada',
            'fecha_rescate': 'Fecha Rescate',
            'sexo': 'Sexo',
            'persona': 'Persona',
            'vacuna': 'Vacuna',
            'tipo_mascota': 'Tipo Mascota'
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
            'tipo_mascota':forms.TextInput(attrs={'class': 'form-control'}),
        }

