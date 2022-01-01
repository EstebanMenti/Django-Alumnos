from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime

from .forms import AlumnoForm
from .models import Alumno

# Create your views here.
def add_alumno(request):
    Alumno.objects.create(first_name=request.GET.get('name', '-'),
                          last_name=request.GET.get('lastname', '-'))
    response = {'status': 'OK'}
    return JsonResponse(response)

@login_required
def get_alumnos(request):
    alumnos = Alumno.objects.all()
    
    form = AlumnoForm( request.POST )
    error = False
    if( form.is_valid() ):
        form.save( commit = True)
    else:
       error = True
    

    
    return render( request, 'alumno_list.html',
            context={'alumnos': alumnos,
                     'now': datetime.datetime.now(),
                     'form': form})
    """
    html = '<html><body><h1>Alumnos<H1>'
    for item in alumnos:
        html += f'<p><a href="/alumnos/{item.id}">{item.last_name}, {item.first_name}</a></p>'
    html += '</body></html>'
    return HttpResponse(html)
    """
@login_required
def alumno(request, id_alumno):
    alumno = Alumno.objects.get(pk=id_alumno)
    form = AlumnoForm( instance=alumno )
    if( request.method == 'POST'):
        form = AlumnoForm(request.POST, instance = alumno)
        if( form.is_valid()):
            form.save(commit=True)    
    return render(request, 'alumno_detail.html',
                  context={'alumno': alumno,
                           'form': form})

    #html = '<html><body><h1>Alumnos<H1>'
    #html += f'<p>Apellido: {alumno.last_name}</p>'docker
    #html += f'<p>Nombre: {alumno.first_name}</p>' 
    #html += '</body></html>'
    #return HttpResponse(html)
