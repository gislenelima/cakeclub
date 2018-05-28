from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #sempre deve ser add para informar ao django
from cakeclub.cakepage import models
from .models import DuplaDaVez, CakePool, Cakes, Dicas
from .forms import CakePoolForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.db.models import Count
from cakeclub.cakepage.forms import DicasForm 
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views hesssssssre.

def home(request):
    return render(request, 'home.html')

def regras(request):
   return render(request,'regras.html')

def listagem_datas(request): 
    posts = DuplaDaVez.objects.all().order_by('-date_da_dupla')
    return render(request, 'datas.html', {'posts':posts})


@method_decorator(login_required, name='dispatch')
class CakePoolCreateView(CreateView):
    model = CakePool
    form_class = CakePoolForm
    template_name = "votacao.html"
    success_url = reverse_lazy('home')#recebe o nome da urls


def resultados(request):
    results = CakePool.objects.all().values('cake__name').annotate(count=Count('cake__name')).order_by('-count')
    return render(request, 'resultados.html',{'results':results})
    #values:agrupa os grupos similares

def dicas(request):
    listar = Dicas.objects.all().order_by('id')
    return render(request, 'dicas.html',{'listar':listar})


class CriarNovaDica (CreateView):
    template_name = 'novadica.html'
    model = Dicas
    form_class = DicasForm
    success_url = reverse_lazy('dicas')


def registar(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/registrar/")
                
        else:
           return render (request, "registrar.html", {"form":form})
              
   
    return render(request, "registrar.html", {"form": UserCreationForm()})
  


def logar (request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            login (request, form.get_user())
            return HttpResponseRedirect("/")

        else: 
            return render(request, "login.html", {"form":form})

    return render(request, "login.html",{"form": AuthenticationForm()})


