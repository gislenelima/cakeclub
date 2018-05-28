from django import forms
from .models import DuplaDaVez, CakePool, Cakes, Dicas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CakePoolForm(forms.ModelForm):
    """Form definition for CakePool."""
    cake = forms.ModelMultipleChoiceField(label='Escolha 3 de seus bolos prediletos',queryset=Cakes.objects.all(),widget = forms.CheckboxSelectMultiple)
    #widget foi utilizado para moldar o formato de apresentação dos campos
    class Meta:
        """Meta definition for CakePoolform."""
        model = CakePool
        fields = ('cake',)

class DicasForm(forms.ModelForm):
    class Meta:
        model = Dicas
        fields = ('titulo','texto')
    

class RegisterForm(UserCreationForm):#está herdando os atribultos de UserCreation e acrescentando email
    
    email = forms.EmailField(label = 'E-mail')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
            return email

    def save (self, commit = True):
        user = super(RegisterForm, self).save(commit = False) 
        user.email = self.cleaned_data['email']
        if commit: 
            user.save()
        return user