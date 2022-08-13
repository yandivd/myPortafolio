from django.contrib import admin
from .models import *

class ProyectoAdmin(admin.ModelAdmin):
    list_display = 'nombre', 'image', 'link', 'categoria'

# Register your models here.
admin.site.register(Proyecto, ProyectoAdmin)
