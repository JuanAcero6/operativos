from dataclasses import fields
from colaProcesos.models import *
from django import forms

class ProcesosForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ('nombre','tiempo','tamaño','prioridad','estado')
    
    nombre = forms.CharField()
    tiempo = forms.IntegerField()
    tamaño = forms.IntegerField()
    prioridad = forms.IntegerField()

    OPCIONES = {
        'EN_ESPERA',"En espera",
        'EN_EJECUCION',"En ejecucion",
        'TERMINADO',"Terminado"
    }

    estado = forms.ChoiceField(
        choices=OPCIONES
    )

    def is_valid(self):
        return super().is_valid()
