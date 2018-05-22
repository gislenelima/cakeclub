from django.contrib import admin
from .models import DuplaDaVez, CakePool, Cakes, Dicas
# Register your models here.

#mostra insformações no admin no formato abaixo

@admin.register(DuplaDaVez)
class DuplaDaVezAdmin(admin.ModelAdmin):
    list_display = ('id','nome_um','nome_dois','date_da_dupla')

@admin.register(Cakes)
class CakesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CakePool)
class CakePoolAdmin(admin.ModelAdmin):
    list_display = ('entry_date',)

@admin.register(Dicas)
class DicasAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    