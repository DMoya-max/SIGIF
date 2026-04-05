from django import forms
from . models import Usuarios 

class UsuarioForm(forms.ModelForm):
    class Meta():
        model = Usuarios
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'})
        }