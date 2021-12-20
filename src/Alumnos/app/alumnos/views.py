from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime

from .models import Alumno

# Create your views here.
def add_alumno(request):
    Alumno.objects.create(first_name=request.GET.get('name', '-'),
                          last_name=request.GET.get('lastname', '-'))
    response = {'status': 'OK'}
    return JsonResponse(response)


def get_alumnos(request):
    alumnos = Alumno.objects.all()
    html = '<html><body><h1>Alumnos<H1>'
    for item in alumnos:
        html += f'<p><a href="/alumnos/{item.id}">{item.last_name}, {item.first_name}</a></p>'
    html += '</body></html>'
    return HttpResponse(html)


def alumno(request, id_alumno):
    alumno = Alumno.objects.get(pk=id_alumno)
    html = '<html><body><h1>Alumnos<H1>'
    html += f'<p>Apellido: {alumno.last_name}</p>'
    html += f'<p>Nombre: {alumno.first_name}</p>' 
    html += '</body></html>'
    return HttpResponse(html)
