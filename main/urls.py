from django.urls import path, include
from .views import index, TestListView, TestimonioCreateView, aceptarTestimonio, eliminarTestimonio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('listar/testimonios/', TestListView.as_view(), name='listado_testimonios' ),
    path('crear/testimonio/', TestimonioCreateView.as_view(), name='crear_testimonio'),

    path('aceptar_testimonio/<id>/', aceptarTestimonio, name='aceptar_testimonio'),
    path('eliminar_testimonio/<id>/', eliminarTestimonio, name='eliminar_testimonio'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)