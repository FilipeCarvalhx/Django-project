from django import forms
from .models import Usuario

class PersonForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'email']

        widgets = {
                'nome': forms.TextInput(attrs={
                    'placeholder': 'Seu nome',
                    'class': 'form-input'
                }),
                'idade': forms.TextInput(attrs={
                    'placeholder': 'Idade',
                    'class': 'form-input'
                }),
                'email': forms.EmailInput(attrs={
                    'placeholder': 'Seu e-mail',
                    'class': 'form-input'
                }),
                
            }