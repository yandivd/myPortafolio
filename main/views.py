from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
import smtplib
from email.mime.text import MIMEText

from django.conf import settings

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
            email=form.cleaned_data['email']
            texto=form.cleaned_data['message']
            messages.success(request, "Gracias por contactarme")
            form.save()
            send_emailC(email, texto)
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
            usuario=formulario.cleaned_data['nombre']
            testi = Testimoni(nombre=formulario.cleaned_data['nombre'],
                              ocupacion=formulario.cleaned_data['ocupacion'],
                              texto=formulario.cleaned_data['texto'],
                              image=image['image'],
                              estado=estado)
            testi.save()
            send_email('Nuevo testimonio', usuario, 'http://localhost:8000/listar/testimonios/')
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

######funcion para enviar correos#######
def send_emailC(email,texto):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        email_to='yandivd@gmail.com'

        #construir el mensaje
        mensaje= MIMEText("""Alguien ha hecho contacto contigo a trves de myPortafolio. 
        Entre al siguiente link para revisarlo: http://localhost:8000/listar/contactos/ """+
                          "Correo: "+email+' '+texto )
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = 'Contacto en myPortafolio'

        mailServer.sendmail(settings.EMAIL_HOST_USER,email_to, mensaje.as_string())
        print("Correo enviado")

    except Exception as e:
        print(e)

def send_email(asunto, usuario, link):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        email_to='yandivd@gmail.com'

        #construir el mensaje
        mensaje= MIMEText(usuario+""" ha dejado un testimonio acerca de ti. Entre al siguiente
                            link para acceder: """+ link)
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = asunto

        mailServer.sendmail(settings.EMAIL_HOST_USER,email_to, mensaje.as_string())
        print("Correo enviado")

    except Exception as e:
        print(e)