from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

# O conteúdo com este slug é exibido na página inicial ("/")
SLUG_INICIO = "inicio"


class Conteudo(models.Model):
    """
    Uma página do portal. O HTML interno da página (somente o miolo:
    <section>, <article>, <h2>, <p>, <img>...) fica guardado no banco.
    A estrutura <html>, <header>, <nav>, <footer> fica nos Templates.
    """

    titulo = models.CharField("título", max_length=200)
    slug = models.SlugField(
        "slug",
        unique=True,
        help_text="Usado na URL, ex.: meu-curriculo → /conteudo/meu-curriculo/",
    )
    conteudo_html = models.TextField(
        "conteúdo HTML",
        help_text="Somente o HTML interno da página (sem <html>, <head>, <body>, "
        "<header>, <nav> ou <footer>).",
    )
    ativo = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "conteúdo"
        verbose_name_plural = "conteúdos"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """URL pública do conteúdo (a página inicial usa a URL '/')."""
        if self.slug == SLUG_INICIO:
            return reverse("home")
        return reverse("conteudo", kwargs={"slug": self.slug})


class Menu(models.Model):
    """
    Um item da navegação do portal.
    Pode apontar para um Conteudo (interno) ou para uma URL (externo).
    """

    class TipoDestino(models.TextChoices):
        INTERNO = "interno", "Conteúdo interno"
        EXTERNO = "externo", "Link externo"

    titulo = models.CharField("título", max_length=100)
    tipo_destino = models.CharField(
        "tipo de destino",
        max_length=10,
        choices=TipoDestino.choices,
        default=TipoDestino.INTERNO,
    )
    ordem = models.PositiveIntegerField(
        "ordem", default=0, help_text="Menor número aparece primeiro."
    )
    ativo = models.BooleanField("ativo", default=True)

    # Relacionamento Menu → Conteudo (usado quando o destino é interno)
    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="itens_menu",
        verbose_name="conteúdo relacionado",
    )
    # Usada quando o destino é externo
    url_externa = models.URLField("URL externa", blank=True)

    class Meta:
        verbose_name = "item de menu"
        verbose_name_plural = "itens de menu"
        ordering = ["ordem", "titulo"]

    def __str__(self):
        return self.titulo

    @property
    def eh_externo(self):
        return self.tipo_destino == self.TipoDestino.EXTERNO

    def get_url(self):
        """Devolve o endereço para onde o item do menu deve levar."""
        if self.eh_externo:
            return self.url_externa
        return self.conteudo.get_absolute_url()

    def clean(self):
        """Regras de validação exibidas no Django Admin."""
        erros = {}
        if self.tipo_destino == self.TipoDestino.INTERNO:
            if not self.conteudo:
                erros["conteudo"] = "Escolha o conteúdo para um link interno."
        elif self.tipo_destino == self.TipoDestino.EXTERNO:
            if not self.url_externa:
                erros["url_externa"] = "Informe a URL para um link externo."
        if erros:
            raise ValidationError(erros)
