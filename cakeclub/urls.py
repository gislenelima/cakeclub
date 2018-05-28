
from django.contrib import admin
from django.urls import path,include
from cakeclub.cakepage import views
from cakeclub.cakepage.views import* 
from cakeclub.cakepage.views import resultados
#from django.contrib.auth.views import 



admin.autodiscover()

urlpatterns = [
   path('',views.home, name = 'home'),
   path('datas/',views.listagem_datas, name = 'datas'),
   path('regras/',views.regras, name = 'regras'),
   path('admin/', admin.site.urls),
   path('voto/', CakePoolCreateView.as_view(), name = 'voto'),  
   path('resultados/', views.resultados, name = 'resultados'),
   path('dicas/', views.dicas, name = 'dicas'),
   path('novadica/', CriarNovaDica.as_view(), name = 'novadica'),
   path('registrar/', views.registar, name = 'registrar'),
  # path('entrar/', django.contrib.auth.views.login, {'template_name':'login.html'}, name = 'login'),
   path('entrar/', views.logar, name = 'login') 
   
]
