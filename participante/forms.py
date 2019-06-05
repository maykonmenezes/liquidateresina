from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import DocumentoFiscal
from localflavor.br.forms import *
from localflavor.br.br_states import STATE_CHOICES


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite seu usuario', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha', 'class':'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Senha*'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirmação de senha*'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Usúario*'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email*'}))
    class Meta:
        model = User
        fields = ('username', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha digitada não é a mesma.')
        return cd['password2']

class ProfileRegistrationForm(forms.ModelForm):
    CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    sexo = forms.ChoiceField(choices=CHOICES_SEXO, widget=forms.Select(attrs={'id' : 'sexo'}))
    estado = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={'id' : 'estados'}))
    pergunta = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Sua resposta'}))
    nome = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Nome Completo*'}))
    RG = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'RG*'}))
    CPF = BRCPFField(required=True, max_length=14, min_length=11, widget=forms.TextInput(attrs={'placeholder':'CPF*',
                                                                                                'class':'cpf'}))
    foneCelular1 = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Celular*',
                                                                                  'class': 'phone_with_ddd'}))
    whatsapp = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Whatsapp',
                                                                                  'class': 'phone_with_ddd'}))
    facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Facebook'}))
    twitter = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Twitter'}) )
    endereco = forms.CharField( required=True, widget=forms.TextInput(attrs={'placeholder':'Endereço*'}))
    enderecoNumero = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Nº da casa'}))
    enderecoComplemento = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Complemento'}))
    bairro = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Bairro*'}))
    cidade = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Cidade*'}))
    estado = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={'id' : 'estados'}))
    CEP = BRZipCodeField(required=False, label='Cep*' , widget=forms.TextInput(attrs={'class':'cep', 'placeholder':'CEP*'}))
    pergunta = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Liquida Teresina'}))
    class Meta:
        model = Profile
        fields = ('nome', 'RG', 'CPF', 'sexo', 'foneFixo', 'foneCelular1', 'foneCelular2', 'foneCelular3',
                  'whatsapp','facebook','twitter','endereco','enderecoNumero','enderecoComplemento', 'estado',
                  'cidade','bairro','CEP','pergunta' )
        exclude = ('user', 'dataCadastro', 'cadastradoPor', 'ativo', 'pendente')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha digitada não é a mesma.')
        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'ativo': forms.HiddenInput,
        }


class UserAddCoupom(forms.ModelForm):
    numeroDoCupom = forms.CharField(label='Numero do cupom')
    valorDoCupom = forms.DecimalField(label='Valor do cupom')

class UserAddFiscalDocForm(forms.ModelForm):
    lojista_cnpj = BRCNPJField(label='CNPJ da loja*', required=True, max_length=18, widget=forms.TextInput(attrs={'class':'cnpj'}))
    dataDocumento = forms.DateField(label='Data*',widget=forms.TextInput(attrs={ 'class':'date'}))
    valorDocumento = forms.DecimalField(label='Valor*')
    numeroDocumento = forms.CharField(label='Número do documento*')
    photo = forms.FileField(label='Documento fiscal', required=False)
    photo2 = forms.FileField(label='Comprovante do cartão', required=False)
    class Meta:
        model = DocumentoFiscal
        fields = ('lojista_cnpj', 'vendedor', 'numeroDocumento', 'dataDocumento', 'valorDocumento', 'compradoMASTERCARD', 'compradoREDE',
                    'photo', 'photo2')
        widgets = {
            #'lojista': forms.HiddenInput,
            'user': forms.HiddenInput,
            'pendente': forms.HiddenInput,
            'observacao': forms.HiddenInput,
            'valorREDE': forms.HiddenInput,
            'valorMASTERCARD': forms.HiddenInput,
            'valorVirtual': forms.HiddenInput,
        }

class DocumentoFiscalEditFormOp(forms.ModelForm):
    class Meta:
        model = DocumentoFiscal
        exclude = ('photo','photo2', 'user', 'lojista')
        fields = '__all__'

class DocumentoFiscalEditForm(forms.ModelForm):
    class Meta:
        model = DocumentoFiscal
        exclude = ('pendente','user', 'lojista', 'observacao')
        fields = '__all__'

class DocumentoFiscalValidaForm(forms.ModelForm):
    class Meta:
        model = DocumentoFiscal
        exclude = ('user','qtdeCupom')
        fields = '__all__'
        widgets = {
            'status': forms.HiddenInput,

        }


class ProfileEditForm(forms.ModelForm):
    CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    sexo = forms.ChoiceField(choices=CHOICES_SEXO, widget=forms.Select(attrs={'id' : 'sexo'}))
    estado = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={'id' : 'estados'}))
    pergunta = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Sua resposta'}))
    nome = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Nome Completo*'}))
    RG = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'RG*'}))
    CPF = BRCPFField(required=True, max_length=14, min_length=11, widget=forms.TextInput(attrs={'placeholder':'CPF*',
                                                                                                'class':'cpf'}))
    foneCelular1 = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Celular*',
                                                                                  'class': 'phone_with_ddd'}))
    whatsapp = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Whatsapp',
                                                                                  'class': 'phone_with_ddd'}))
    facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Facebook'}))
    twitter = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Twitter'}) )
    endereco = forms.CharField( required=True, widget=forms.TextInput(attrs={'placeholder':'Endereço*'}))
    enderecoNumero = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Nº da casa'}))
    enderecoComplemento = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Complemento'}))
    bairro = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Bairro*'}))
    cidade = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Cidade*'}))
    estado = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={'id' : 'estados'}))
    CEP = BRZipCodeField(required=False, label='Cep*' , widget=forms.TextInput(attrs={'class':'cep', 'placeholder':'CEP*'}))
    pergunta = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Liquida Teresina'}))
    class Meta:
        model = Profile
        fields = ('nome', 'RG', 'CPF', 'sexo', 'foneFixo', 'foneCelular1', 'foneCelular2', 'foneCelular3',
                  'whatsapp','facebook','twitter','endereco','enderecoNumero','enderecoComplemento', 'estado',
                  'cidade','bairro','CEP','pergunta' )
        exclude = ('user', 'dataCadastro', 'cadastradoPor', 'ativo', 'pendente')
