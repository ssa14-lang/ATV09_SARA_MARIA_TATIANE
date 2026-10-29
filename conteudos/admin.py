from django.contrib import admin

from .models import Conteudo, Menu


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "ativo")
    list_editable = ("ativo",)
    list_filter = ("ativo",)
    search_fields = ("titulo", "slug")
    # O slug é preenchido automaticamente a partir do título
    prepopulated_fields = {"slug": ("titulo",)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ordem", "tipo_destino", "conteudo", "url_externa", "ativo")
    list_display_links = ("titulo",)
    # Permite mudar ordem e ativar/desativar direto na listagem
    list_editable = ("ordem", "ativo")
    list_filter = ("tipo_destino", "ativo")
    ordering = ("ordem", "titulo")
