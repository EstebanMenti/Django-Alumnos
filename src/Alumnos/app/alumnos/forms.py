from django import forms
from django.forms import ModelForm

from .models import Alumno

class AlumnoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for dic in self.fields.keys():
            self.fields[ dic ].widget.attrs.update({'class':'form-control'})

        self.fields[ 'curso' ].widget.attrs.update({'class':'form-select'})
        self.fields[ 'status' ].widget.attrs.update({'class':'form-select'})

                
    class Meta:
        model = Alumno
        fields = ['first_name', 'last_name', 'curso', 'status','birthday']

"""
class AlumnoForm(forms.Form):
    #Ver si se puede traer los atrivitos del modelo
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthday = forms.DateTimeField()

    def save(self, commit = False):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        birthday = self.cleaned_data['birthday']
        alumnos = Alumno(first_name = first_name, last_name = last_name, 
                         birthday = birthday)
        if( commit == True):
            alumnos.save()
        return alumnos
"""        