from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .models import Conteudo, Menu


class PortalTests(TestCase):
    def setUp(self):
        self.inicio = Conteudo.objects.create(
            titulo="Início", slug="inicio", conteudo_html="<h2>Bem-vindos</h2>"
        )
        self.curriculo = Conteudo.objects.create(
            titulo="Meu Currículo", slug="meu-curriculo", conteudo_html="<h2>Currículo</h2>"
        )
        Menu.objects.create(titulo="Início", ordem=1, conteudo=self.inicio)
        Menu.objects.create(titulo="Currículo", ordem=2, conteudo=self.curriculo)
        Menu.objects.create(
            titulo="GitHub",
            tipo_destino=Menu.TipoDestino.EXTERNO,
            url_externa="https://github.com/",
            ordem=3,
        )

    def test_home_exibe_html_do_banco(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "<h2>Bem-vindos</h2>", html=True)

    def test_conteudo_por_slug(self):
        resposta = self.client.get("/conteudo/meu-curriculo/")
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "<h2>Currículo</h2>", html=True)

    def test_menu_dinamico_com_links_internos_e_externos(self):
        resposta = self.client.get("/")
        self.assertContains(resposta, 'href="/conteudo/meu-curriculo/"')
        self.assertContains(resposta, 'href="https://github.com/"')

    def test_item_inativo_nao_aparece_no_menu(self):
        Menu.objects.filter(titulo="GitHub").update(ativo=False)
        resposta = self.client.get("/")
        self.assertNotContains(resposta, "https://github.com/")

    def test_ordem_do_menu(self):
        Menu.objects.filter(titulo="GitHub").update(ordem=0)
        resposta = self.client.get("/")
        itens = [m.titulo for m in resposta.context["menu_itens"]]
        self.assertEqual(itens, ["GitHub", "Início", "Currículo"])

    def test_conteudo_inativo_da_404_e_some_do_menu(self):
        Conteudo.objects.filter(slug="meu-curriculo").update(ativo=False)
        self.assertEqual(self.client.get("/conteudo/meu-curriculo/").status_code, 404)
        self.assertNotContains(self.client.get("/"), "/conteudo/meu-curriculo/")

    def test_slug_inexistente_da_404(self):
        self.assertEqual(self.client.get("/conteudo/nao-existe/").status_code, 404)

    def test_validacao_do_menu(self):
        interno_sem_conteudo = Menu(titulo="X", tipo_destino=Menu.TipoDestino.INTERNO)
        with self.assertRaises(ValidationError):
            interno_sem_conteudo.full_clean()
        externo_sem_url = Menu(titulo="Y", tipo_destino=Menu.TipoDestino.EXTERNO)
        with self.assertRaises(ValidationError):
            externo_sem_url.full_clean()
