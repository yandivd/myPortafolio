from django.conf import settings
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='proyectos')
    link = models.CharField(max_length=400)
    # categoria = models.CharField(max_length=20)
    # categoria = models.ManyToManyField(Categoria)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

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
    estado = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'

    def get_image(self):
        if self.image:
            return '{}{}'.format(settings.MEDIA_URL, self.image)
        else:
            return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')

class Contacto(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
