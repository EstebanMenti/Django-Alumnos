from django.db import models

# Create your models here.

class Alumno(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name.title()}, {self.first_name.title()}'
