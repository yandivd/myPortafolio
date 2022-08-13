from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    proyectos = Proyecto.objects.all()
    data={
        'proyectos': proyectos
    }
    return render(request, 'main/index.html', data)
