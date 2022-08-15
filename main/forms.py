from django import forms
from .models import Contacto, Testimoni, Proyecto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'