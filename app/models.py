from django.db import models

# Create your models here.

class Tipo_contacto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    tipo_contacto = models.ForeignKey(Tipo_contacto, on_delete=models.PROTECT)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
   
class Insumo(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="insumo", null=True, blank=True)
    descripcion = models.TextField( max_length=200)
    stock = models.IntegerField()
  
    

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to="servicio", null=True)

    def __str__(self):
        return self.nombre



class Slider(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    imagen = models.ImageField(upload_to="slider")

    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    nombre = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to="galeria")

    def __str__(self):
        return self.nombre

class Nosotros(models.Model):
    fecha = models.DateField()
    nosotros = models.TextField(max_length=500)
    historia = models.TextField()
    mision = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.nosotros