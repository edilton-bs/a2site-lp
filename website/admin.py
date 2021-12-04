from django.contrib import admin
from website.models import Materias, Usuario

admin.site.register(Materias)


# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "sexo", "idade")
    
    
admin.site.register(Usuario, UsuarioAdmin)