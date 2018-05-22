from django import forms
from .models import DuplaDaVez, CakePool, Cakes, Dicas


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
    

       