from django.db import models


# Create your models here.
class Curso(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.name.title()}'


class Alumno(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #Genera una referencia a otra tablaº
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, 
                              null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.last_name.title()}, {self.first_name.title()}'
