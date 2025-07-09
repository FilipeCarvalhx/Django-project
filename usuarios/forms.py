from django import forms
from .models import Usuario

class PersonForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'email']