from django.db import models


# Create your models here.
class Curso(models.Model):
    name = models.CharField(max_length = 30)
    date_create = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.name.title()}'

class Alumno(models.Model):
    STATUS_CHOINES = (
        ('A', 'Activo'),
        ('B', 'Baja'),
        ('C','Cursando'),
    )
    first_name = models.CharField('Nombre', max_length=30 )
    last_name = models.CharField('Apellido', max_length=30 )
    #Genera una referencia a otra tablaº
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, 
                              null=True, blank=True)
    status = models.CharField('Estado', max_length=4, choices = STATUS_CHOINES,
                               default='A', blank=True)                          
    birthday = models.DateTimeField('Fecha Nacimiento', null=True )
    date_create = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.last_name.title()}, {self.first_name.title()}'
