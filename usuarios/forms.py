from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    nome_completo = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=100, required=True)
    telefone = forms.CharField(max_length=9, required=True)
    
    class Meta:
        
        model = User
        fields = UserCreationForm.Meta.fields + ('telefone')
