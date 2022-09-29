from django.shortcuts import render
from colaProcesos.forms import *

def home(request):
    from icecream import ic
    ic(request.POST)
    formulario = ProcesosForm(
        request.POST or None
    )
    ic(formulario)
    procesos = Proceso.objects.all()
    memorias = Memoria.objects.all()
    memoria_valid = False
    if memorias:
        memoria_valid = True
    if request.POST:
        if request.POST.get('tamaño_memoria'):
            memorias.all().delete()
            memoria = Memoria()
            memoria.tamaño = request.POST.get('tamaño_memoria')
            memoria.save()
        elif request.POST.get('eliminar'):
            memorias.all().delete()
        else:
            proceso = Proceso()
            proceso.nombre = request.POST.get('nombre')
            proceso.tiempo = request.POST.get('tiempo')
            proceso.tamaño = request.POST.get('tamaño')
            proceso.prioridad = request.POST.get('prioridad')
            proceso.estado = Proceso.EN_ESPERA
            proceso.save()
        return render(request,'home.html', {
            'formulario':formulario, 
            'procesos':procesos,
            'memorias':memorias,
            'memoria_valid': memoria_valid
        })
    return render(request,'home.html', {
        'formulario':formulario, 
        'procesos':procesos, 
        'memorias':memorias,
        'memoria_valid': memoria_valid
    })

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def simulacion(request):       
    procesos = Proceso.objects.all()
    memorias = Memoria.objects.all()
    tamaño = 0
    for memoria in memorias:
        tamaño = memoria.tamaño
    diccionario = []

    for proceso in procesos:
        dicc = {
            'Id':proceso.pk,
            'Tamaño_usado':proceso.tamaño,
            'Nombre':proceso.nombre,
            'Tiempo_restante':proceso.tiempo,
            'Prioridad':proceso.prioridad,
            'Estado':proceso.get_estado_display()
        }
        diccionario.append(dicc)       

    return render(request,'simulacion.html', {
        'diccionario':diccionario,
        'memorias':memorias,
        'tamaño':tamaño
    })
