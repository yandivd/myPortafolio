from django.contrib import admin
from .models import *

class ProyectoAdmin(admin.ModelAdmin):
    list_display = 'nombre', 'image', 'link', 'categoria'

class TestimonioAdmin(admin.ModelAdmin):
    list_display = 'nombre', 'ocupacion', 'image', 'texto'

# Register your models here.
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Testimoni, TestimonioAdmin)
