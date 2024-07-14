from django.urls import path, include
from .views import (
    inicio, contacto, ultima, nacional, internacional, tiempo, 
    CustomLoginView, registrarse, subirNoticia, listar, agrega_form, 
    editar, eliminar, listar_usuarios, eliminar_usuario, 
    nuevo_usuario, registro
)

urlpatterns = [
    path('', inicio, name="inicio"),
    path('contacto', contacto, name="contacto"),
    path('ultima', ultima, name="ultima"),
    path('nacional', nacional, name="nacional"),
    path('internacional', internacional, name="internacional"),
    path('tiempo', tiempo, name="tiempo"),
    path('login', CustomLoginView.as_view(), name="login"),  # Vista personalizada de login
    path('registrarse', registrarse, name="registrarse"),
    path('subirnoticia', subirNoticia, name="subirnoticia"),
    path('listar/', listar, name='listar'),  
    path('agrega_form/', agrega_form, name='agrega_form'),
    path('editar/<int:pk>/', editar, name='editar'),
    path('eliminar/<int:pk>/', eliminar, name='eliminar'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('eliminar_usuario/<int:pk>/', eliminar_usuario, name='eliminar_usuario'),
    path('nuevo_usuario/', nuevo_usuario, name='nuevo_usuario'),
    path('registro/', registro, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),
]
