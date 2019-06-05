from django.contrib import admin
from .models import Cupom
# Register your models here.
class CupomAdmin(admin.ModelAdmin):
    list_display = ( 'id','user', 'documentoFiscal', 'operador', 'dataCriacao', 'impresso', 'dataImpressao')
    search_fields = ( 'documentoFiscal__numeroDocumento','id', 'user__username')

admin.site.register(Cupom, CupomAdmin)
