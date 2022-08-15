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

class Testimoni(models.Model):
    nombre = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonios', blank=True, null=True)
    texto = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
