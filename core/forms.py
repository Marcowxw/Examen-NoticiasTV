from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import SubirN, Profile

class SubirNForm(forms.ModelForm):
    class Meta:
        model = SubirN
        fields = ['titulo', 'pNombre', 'pApellido', 'seleccion', 'categoria', 'imagen', 'descripcion']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rut = forms.CharField(max_length=12)
    fecha_nacimiento = forms.DateField()
    genero = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=100)
    comuna = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'rut', 'fecha_nacimiento', 'genero', 'direccion', 'comuna', 'telefono']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile(
                user=user,
                rut=self.cleaned_data['rut'],
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                genero=self.cleaned_data['genero'],
                direccion=self.cleaned_data['direccion'],
                comuna=self.cleaned_data['comuna'],
                telefono=self.cleaned_data['telefono'],
            )
            profile.save()
        return user

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
