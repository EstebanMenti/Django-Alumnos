from django.urls import path

from .views import add_alumno, get_alumnos, alumno


urlpatterns = [
    path('', get_alumnos),
    path('add', add_alumno),
    path('id', alumno),
]