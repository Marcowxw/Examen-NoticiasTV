from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia, SubirN, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import SubirNForm, RegistroForm, CustomLoginForm

def inicio(request):
    return render(request, 'core/inicio.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def ultima(request):
    return render(request, 'core/ultima.html')

def nacional(request):
    return render(request, 'core/nacional.html')

def internacional(request):
    return render(request, 'core/internacional.html')

def tiempo(request):
    return render(request, 'core/tiempo.html')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Crear perfil si no existe
        if not hasattr(self.request.user, 'profile'):
            Profile.objects.create(user=self.request.user)
        return response

def registrarse(request):
    return render(request, 'core/registrarse.html')

def subirNoticia(request):
    return render(request, 'core/subirnoticia.html')

def listar(request):
    noticias = SubirN.objects.all()
    return render(request, 'core/listar.html', {'noticias': noticias})

def eliminar(request, pk):
    noticia = get_object_or_404(SubirN, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('listar')
    return render(request, 'core/confirmar_eliminar.html', {'noticia': noticia})

def editar(request, pk):
    noticia = get_object_or_404(SubirN, pk=pk)
    if request.method == 'POST':
        form = SubirNForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = SubirNForm(instance=noticia)
    return render(request, 'core/editar.html', {'form': form})

def agrega_form(request):
    if request.method == 'POST':
        form = SubirNForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = SubirNForm()
    context = {
        'form': form
    }
    return render(request, 'core/agrega_form.html', context)

def listar_usuarios(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'core/listar_usuarios.html', context)

def eliminar_usuario(request, pk):
    try:
        usuario = User.objects.get(id=pk)
        usuario.delete()
        mensaje = "Usuario eliminado exitosamente!!!!"
        usuarios = User.objects.all()
        context = {
            'usuarios': usuarios,
            'mensaje': mensaje
        }
        return render(request, 'core/listar_usuarios.html', context)
    except User.DoesNotExist:
        mensaje = "Usuario no existente!!!!"
        usuarios = User.objects.all()
        context = {
            'usuarios': usuarios,
            'mensaje': mensaje
        }
        return render(request, 'core/listar_usuarios.html', context)

def nuevo_usuario(request):
    if request.method == 'POST':
        usuario = User.objects.create_user(
            first_name=request.POST['nombre'],
            last_name=request.POST['apellido'],
            username=request.POST['username'],
            password=request.POST['contrasena'],
            email=request.POST['correo']
        )
        Profile.objects.create(
            user=usuario,
            rut=request.POST['rut'],
            fecha_nacimiento=request.POST['fecha_nacimiento'],
            genero=request.POST['sexo'],
            direccion=request.POST['direccion'],
            comuna=request.POST['comuna'],
            telefono=request.POST['numeroT']
        )
        mensaje = "Nuevo usuario guardado exitosamente."
        context = {
            'mensaje': mensaje
        }
        return render(request, 'core/subir_usuario.html', context)
    else:
        return render(request, 'core/subir_usuario.html')

#--------------------------------  Registro de usuario.  -----------------------------------


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})