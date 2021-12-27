from django.contrib import admin

# Register your models here.
from .models import Alumno, Curso


admin.site.register(Alumno)
admin.site.register(Curso)
