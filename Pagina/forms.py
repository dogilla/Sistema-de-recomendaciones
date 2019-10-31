from django.forms import ModelForm
from Pagina.models import Pagina

class PaginaForm(ModelForm):
    class Meta:
        model = Pagina
        fields = ['recomendacion']
        
