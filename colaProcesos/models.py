from email.policy import default
from django.db import models

"""
    Modelo que se va a usar para el manejo de los procesos
"""

class Proceso(models.Model):

    class Meta:
        verbose_name = 'Proceso'
        verbose_name_plural = 'Procesos'

    nombre = models.CharField(max_length=250, null=True, blank=True)
    tiempo = models.IntegerField(null=True,blank=True)
    tiempo_restante = models.IntegerField(null=True,blank=True,default=0)
    tamaño = models.IntegerField(null=True,blank=True)

    prioridad =  models.SmallIntegerField(default=0)
    EN_ESPERA = 0
    EN_EJECUCION = 1
    TERMINADO = 2
    OPCIONES = (
        ( EN_ESPERA, "En espera"),
        ( EN_EJECUCION, "En ejecucion"),
        ( TERMINADO, "Terminado")
    )

    estado = models.SmallIntegerField(choices=OPCIONES, default=EN_ESPERA)  


class Memoria(models.Model):

    class Meta:
        verbose_name = 'Memoria'

    tamaño = models.IntegerField(null=True,blank=True)  