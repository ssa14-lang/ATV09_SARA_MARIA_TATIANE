# ATV09 — Migração do Portal para Django

## Identificação do grupo

- **Integrante 1:** Sara da Silva Alves
- **Integrante 2:** Maria Clara de Melo Silva
- **Integrante 3:** Tatiane Severo dos Santos
- **Turma:** 523
- **Disciplina:** Desenvolvimento Web

## Descrição do projeto

Migração do portal desenvolvido na ATV06 (HTML semântico, CSS, Flexbox e design
responsivo) para uma aplicação **Django**. O menu e os conteúdos deixaram de ser
escritos diretamente no HTML e passaram a ser **dados cadastrados no banco e
administráveis pelo Django Admin**:

- **Conteudo**: guarda título, slug, HTML interno da página e se está ativo.
- **Menu**: guarda título, tipo de destino (conteúdo interno ou link externo), ordem,
  se está ativo, o relacionamento com `Conteudo` (links internos) e a URL (links externos).
- O menu é **gerado dinamicamente** a partir do Model `Menu`.
- Cada conteúdo é aberto por uma URL dinâmica baseada no slug: `/conteudo/<slug>/`.

## Tecnologias utilizadas

- Python 3
- Django
- SQLite
- HTML5 semântico, CSS3 (Flexbox + Media Queries)
- Git e GitHub

## Como executar o projeto

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

Windows (CMD):

```cmd
venv\Scripts\activate.bat
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Executar as migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar o superusuário

```bash
python manage.py createsuperuser
```

### 5. Cadastrar os dados iniciais (conteúdos e menu)

```bash
python manage.py popular_dados
```

Esse comando grava no banco 7 conteúdos e 9 itens de menu (7 internos + 2 externos).
Depois disso tudo pode ser alterado pelo Django Admin.

### 6. Executar o servidor

```bash
python manage.py runserver
```

### 7. Acessar

- **Aplicação:** http://127.0.0.1:8000/
- **Django Admin:** http://127.0.0.1:8000/admin/ (use o superusuário criado no passo 4)

### Testes automatizados (opcional)

```bash
python manage.py test
```

## Estrutura do projeto

```
ATV09_SARA_MARIA_TATIANE/
├── manage.py
├── requirements.txt
├── portal/                  # projeto Django (settings, urls)
└── conteudos/               # aplicação Django
    ├── models.py            # Conteudo e Menu
    ├── admin.py             # Models no Django Admin
    ├── views.py             # home, conteudo_detalhe, obter_itens_menu
    ├── urls.py              # "/" e "conteudo/<slug>/"
    ├── migrations/
    ├── templates/conteudos/ # base.html, home.html, conteudo.html
    ├── static/conteudos/    # css/, img/, js/
    ├── seed/                # HTML inicial dos conteúdos
    └── management/commands/popular_dados.py
```
