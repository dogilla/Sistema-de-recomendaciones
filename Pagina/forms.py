from django.forms import ModelForm
from Pagina.models import Pagina

class PaginaForm(ModelForm):
    """
    Clase de representa un campo de texto para introducir el nombre de la aplicación

    """
    class Meta:
        """
        atributos
        ---------

        model:
            modelo al que hace alucion la clase PaginaForm
        fields:
            campo de recomendacion
        """
        model = Pagina
        fields = ['recomendacion']
        
