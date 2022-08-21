from email.mime.text import MIMEText

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
import smtplib

from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all()
    testimonios = Testimoni.objects.all().filter(estado="check")
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
            # send_email(form.cleaned_data['email'])
            return redirect(to='index')
        else:
            data["form"] = form


    return render(request, 'main/index.html', data)

class TestListView(ListView):
    model = Testimoni
    template_name = 'main/testimonios/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = Testimoni.objects.all().filter(estado="pending")

        return context

class ContactoListView(ListView):
    model = Contacto
    template_name = 'main/contactos/list.html'

class TestimonioCreateView(CreateView):
    model = Testimoni
    form_class = TestimonioFOrm
    template_name = 'main/testimonios/create.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        formulario = TestimonioFOrm(data=request.POST)
        #imagen= request.FILES
        image=request.FILES
        print(image.values())
        estado="pending"
        if formulario.is_valid():
            testi = Testimoni(nombre=formulario.cleaned_data['nombre'],
                              ocupacion=formulario.cleaned_data['ocupacion'],
                              texto=formulario.cleaned_data['texto'],
                              image=image['image'],
                              estado=estado)
            testi.save()
            messages.success(request, "Muchas gracias por compartir su testimonio, una vez sea revisado se hara publico")
            return redirect('index')
        else:
            messages.error(request, "Formulario contiene datos no validos")
            return redirect('index')

def aceptarTestimonio(request,id):
    testimonio = Testimoni.objects.get(id=id)
    testimonio.estado = "check"
    testimonio.save()
    return redirect(to='listado_testimonios')

def eliminarTestimonio(request,id):
    testimonio = Testimoni.objects.get(id=id)
    print(testimonio)
    testimonio.delete()
    return redirect(to='listado_testimonios')
#
# def send_email(from1):
#     mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
#     mailServer.starttls()
#     mailServer.ehlo()
#     mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#
#     mensaje = MIMEText("""Mensaje""")
#     mensaje['From'] = from1
#     mensaje['To'] = 'yandivd@gmail.com'
#     mensaje['Subject'] = 'Tienes un correo'