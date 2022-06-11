from django.contrib import admin

from gestionPedidos.models import Client, Article, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "mobile")
    search_fields = ('name','mobile')


admin.site.register(Client, ClientAdmin)
admin.site.register(Article)
admin.site.register(Order)
