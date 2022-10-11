from django import forms
from .models import Contacto, Testimoni

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class TestimonioFOrm(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = 'nombre','ocupacion','image','texto'