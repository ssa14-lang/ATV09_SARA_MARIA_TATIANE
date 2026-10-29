"""
Comando: python manage.py popular_dados

Cria (ou atualiza) os Conteúdos e os itens de Menu iniciais do portal.
O HTML de cada conteúdo é lido da pasta conteudos/seed/ e GRAVADO NO BANCO.
Depois disso, tudo pode ser alterado pelo Django Admin.
"""
from pathlib import Path

from django.core.management.base import BaseCommand

from conteudos.models import Conteudo, Menu

PASTA_SEED = Path(__file__).resolve().parents[2] / "seed"

# (slug, título do conteúdo, título no menu)
CONTEUDOS = [
    ("inicio", "Início", "Início"),
    ("curriculo-sara", "Currículo - Sara da Silva Alves", "Currículo de Sara"),
    ("tema-sara", "Músicas para Treinar", "Tema Livre de Sara"),
    ("curriculo-maria-clara", "Currículo - Maria Clara de Melo Silva", "Currículo de Maria Clara"),
    ("tema-maria-clara", "The Mentalist", "Tema Livre de Maria Clara"),
    ("curriculo-tatiane", "Currículo - Tatiane Severo dos Santos", "Currículo de Tatiane"),
    ("tema-tatiane", "The Chosen", "Tema Livre de Tatiane"),
]

LINKS_EXTERNOS = [
    ("GitHub", "https://github.com/"),
    ("W3Schools", "https://www.w3schools.com/"),
]


class Command(BaseCommand):
    help = "Cadastra os conteúdos e itens de menu iniciais do portal."

    def handle(self, *args, **options):
        ordem = 1

        for slug, titulo, titulo_menu in CONTEUDOS:
            html = (PASTA_SEED / f"{slug}.html").read_text(encoding="utf-8")
            conteudo, _ = Conteudo.objects.update_or_create(
                slug=slug,
                defaults={"titulo": titulo, "conteudo_html": html, "ativo": True},
            )
            Menu.objects.update_or_create(
                titulo=titulo_menu,
                defaults={
                    "tipo_destino": Menu.TipoDestino.INTERNO,
                    "conteudo": conteudo,
                    "url_externa": "",
                    "ordem": ordem,
                    "ativo": True,
                },
            )
            ordem += 1

        for titulo_menu, url in LINKS_EXTERNOS:
            Menu.objects.update_or_create(
                titulo=titulo_menu,
                defaults={
                    "tipo_destino": Menu.TipoDestino.EXTERNO,
                    "conteudo": None,
                    "url_externa": url,
                    "ordem": ordem,
                    "ativo": True,
                },
            )
            ordem += 1

        self.stdout.write(self.style.SUCCESS(
            f"{Conteudo.objects.count()} conteúdos e {Menu.objects.count()} itens de menu cadastrados."
        ))
