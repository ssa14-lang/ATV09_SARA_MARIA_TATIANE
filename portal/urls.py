"""
URLs principais do projeto.
Aqui só "encaixamos" o Admin e as URLs da aplicação conteudos.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("conteudos.urls")),
]
