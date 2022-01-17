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

#@login_required
def get_alumnos(request):
    alumnos = Alumno.objects.all()
    error = False
    # if this is a POST request we need to process the form data
    if( request.method == 'POST'):
        # create a form instance and populate it with data from the request:
        form = AlumnoForm( request.POST )
        # check whether it's valid:
        if( form.is_valid() ):
            form.save( commit = True)
        else:
            error = True
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlumnoForm( )
    
    return render( request, 'alumno_list.html',
            context={'alumnos': alumnos,
                     'now': datetime.datetime.now(),
                     'form': form,
                     'error':error})

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

