from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    proyectos = Proyecto.objects.all()
    testimonios = Testimoni.objects.all()
    for i in testimonios:
        print(i)
    data={
        'proyectos': proyectos,
        'testimonios': testimonios,
    }
    return render(request, 'main/index.html', data)
