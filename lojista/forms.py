from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Lojista, RamoAtividade
from localflavor.br.forms import *

class LojistaRegistrationForm(forms.ModelForm):
    CNPJLojista = BRCNPJField(label='CNPJ*', required=True, max_length=18, widget=forms.TextInput(attrs={'class':'cnpj'}))
    ramoAtividade =  forms.Select(attrs={'class':'form-group'}) 
    class Meta:
        model = Lojista
        fields = '__all__'
        widgets = {
            'ativo': forms.HiddenInput,
            'CadastradoPor': forms.HiddenInput,
        }

class RamoAtividadeRegistrationForm(forms.ModelForm):

    class Meta:
        model = RamoAtividade
        fields = '__all__'
        widgets = {
            'CadastradoPor': forms.HiddenInput,
        }
