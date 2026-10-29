"""
Configurações do projeto Django "portal" (ATV09).
"""
from pathlib import Path

# Pasta raiz do projeto (onde está o manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave de desenvolvimento (apenas para uso em aula; nunca usar em produção)
SECRET_KEY = "django-insecure-atv09-chave-apenas-para-desenvolvimento"

DEBUG = True

ALLOWED_HOSTS = []

# Aplicações instaladas. "conteudos" é a nossa aplicação.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "conteudos",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # APP_DIRS=True faz o Django procurar templates em conteudos/templates/
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portal.wsgi.application"

# Banco de dados: SQLite (arquivo db.sqlite3 na raiz do projeto)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Idioma e fuso horário (Django Admin em português)
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Maceio"
USE_I18N = True
USE_TZ = True

# Arquivos estáticos (CSS, imagens, JS) ficam em conteudos/static/conteudos/
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
