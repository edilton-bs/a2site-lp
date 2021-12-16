from django.contrib import admin
from website.models import Materias, Usuario, Comb_materias, Gatos

admin.site.register(Materias)


# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "sexo", "idade")
    
    
admin.site.register(Usuario, UsuarioAdmin)

class GatosAdmin(admin.ModelAdmin):
    list_display = ("nome", "sexo")
    
    
admin.site.register(Gatos, GatosAdmin)




class Comb_materiasAdmin(admin.ModelAdmin):
    list_display = ("mat1", "mat2", "mat3", "mat4", "mat5", "mat6", "mat7", "mat8", "mat9", "mat10")
    
    
admin.site.register(Comb_materias, Comb_materiasAdmin)