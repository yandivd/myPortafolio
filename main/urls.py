from django.urls import path, include
from .views import index, TestListView, TestimonioCreateView

urlpatterns = [
    path('', index, name='index'),
    path('listar/testimonios/', TestListView.as_view(), name='listado_testimonios' ),
    path('crear/testimonio/', TestimonioCreateView.as_view(), name='crear_testimonio'),
]