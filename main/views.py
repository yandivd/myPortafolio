from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all()
    testimonios = Testimoni.objects.all()
    data={
        'proyectos': proyectos,
        'testimonios': testimonios,
        'form':ContactoForm(),
    }
    if request.method == 'POST':
        form = ContactoForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "Gracias por contactarme")
            form.save()
            return redirect(to='index')
        else:
            data["form"] = form


    return render(request, 'main/index.html', data)

class TestListView(ListView):
    model = Testimoni
    template_name = 'main/testimonios/list.html'
