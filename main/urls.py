from django.urls import path, include
from .views import index, TestimonioCreateView

urlpatterns = [
    path('', index, name='index'),
    path('crear/testimonio/', TestimonioCreateView.as_view(), name='crearTest'),
]