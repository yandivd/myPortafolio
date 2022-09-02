from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import FormView, RedirectView

# Create your views here.
def avs(request):
    pass
class LoginFormView(FormView):
    form_class=AuthenticationForm
    template_name='login.html'
    success_url=reverse_lazy('index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context    

class LogoutRedirectView(RedirectView):
    pattern_name='index'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)