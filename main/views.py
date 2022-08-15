from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all()
    testimonios = Testimoni.objects.all()
    for i in testimonios:
        print(i)
    data={
        'proyectos': proyectos,
        'testimonios': testimonios,
        'form':ContactoForm(),
    }
    if request.method == 'POST':
        form = ContactoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
        else:
            data["form"] = form


    return render(request, 'main/index.html', data)
