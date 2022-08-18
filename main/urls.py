from django.urls import path, include
from .views import index, TestListView

urlpatterns = [
    path('', index, name='index'),
    path('listar/testimonios/', TestListView.as_view(), name='listado_testimonios' ),
]