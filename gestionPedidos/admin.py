from django.contrib import admin

from gestionPedidos.models import Client, Article, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "mobile")
    search_fields = ('name','mobile')


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('section',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'date')
    list_filter = ('date',)
    date_hierarchy = 'date'


# Pruebas
admin.site.register(Client, ClientAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Order, OrderAdmin)
