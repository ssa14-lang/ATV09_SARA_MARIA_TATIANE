from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import SLUG_INICIO, Conteudo, Menu


def obter_itens_menu():
    """
    Busca no banco os itens do menu que devem aparecer no portal:
    - somente itens ativos;
    - links internos só aparecem se o conteúdo relacionado também estiver ativo.
    A ordem vem do Meta do Model (campo 'ordem').
    """
    return (
        Menu.objects.filter(ativo=True)
        .filter(Q(tipo_destino=Menu.TipoDestino.EXTERNO) | Q(conteudo__ativo=True))
        .select_related("conteudo")
    )


def home(request):
    """Página inicial: exibe o conteúdo com slug 'inicio'."""
    conteudo = get_object_or_404(Conteudo, slug=SLUG_INICIO, ativo=True)
    contexto = {"conteudo": conteudo, "menu_itens": obter_itens_menu()}
    return render(request, "conteudos/home.html", contexto)


def conteudo_detalhe(request, slug):
    """Exibe um conteúdo específico, buscado pelo slug da URL."""
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)
    contexto = {"conteudo": conteudo, "menu_itens": obter_itens_menu()}
    return render(request, "conteudos/conteudo.html", contexto)
