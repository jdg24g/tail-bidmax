from django.contrib import admin
from .models import Producto, Cliente, Ticket, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0

    def get_extra(self,request,obj=None,**kwargs):
        if obj is None or not obj.itempedido_set.exists():
            return 1
        return 0
    
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ['cliente', 'tipo', 'add_time']
    
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(ItemPedido)


admin.site.site_header = 'BIDMAX'
admin.site.site_title = 'BIDMAX'
admin.site.index_title = 'BIDMAX'