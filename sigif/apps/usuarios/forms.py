from . forms import Form
from . models import Usuarios 

class UsuarioForm(Form.ModelForm):
    class Meta():
        model = Usuarios
        fields = '__all__'