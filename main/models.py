from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='proyectos')
    link = models.CharField(max_length=400)
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
