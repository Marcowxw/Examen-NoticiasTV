from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class SubirN(models.Model):
    titulo = models.CharField(max_length=100)
    pNombre = models.CharField(max_length=50)
    pApellido = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    seleccion = models.CharField(max_length=20)
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='core/img')
    descripcion = models.CharField(max_length=200) 
    def __str__(self):
        return f"{self.titulo}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
