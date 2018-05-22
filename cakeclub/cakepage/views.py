from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #sempre deve ser add para informar ao django
from cakeclub.cakepage import models
from .models import DuplaDaVez, CakePool, Cakes, Dicas
from .forms import CakePoolForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.db.models import Count
from cakeclub.cakepage.forms import DicasForm 
# Create your views here.

def home(request):
    return render(request, 'home.html')

def regras(request):
   return render(request,'regras.html')

def listagem_datas(request): 
    posts = DuplaDaVez.objects.all()
    return render(request, 'datas.html', {'posts':posts})

class CakePoolCreateView(CreateView):
    model = CakePool
    form_class = CakePoolForm
    template_name = "votacao.html"
    success_url = reverse_lazy('home')#recebe o nome da urls


def resultados(request):
    results = CakePool.objects.all().values('cake__name').annotate(count=Count('cake__name'))
    return render(request, 'resultados.html',{'results':results})


def dicas(request):
    listar = Dicas.objects.all().order_by('id')
    return render(request, 'dicas.html',{'listar':listar})


class CriarNovaDica (CreateView):
    template_name = 'novadica.html'
    model = Dicas
    form_class = DicasForm
    success_url = reverse_lazy('dicas')


# class ListarNovaDica (ListView):
#     model = Dicas
    
#     def get_queryset(self):
#         queryset = Dicas.objects.all()
    
   


