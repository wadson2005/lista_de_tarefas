# Lista de Tarefas (Django)

Aplicacao web simples para gerenciar tarefas com Django.

## Funcionalidades

- Criar tarefa
- Marcar tarefa como concluida
- Excluir tarefa (com confirmacao)

## Tecnologias

- Python
- Django 5
- SQLite3
- Bootstrap 4 (via CDN)

## Requisitos

- Python 3.10+
- pip

## Como executar

- Passo 1: Clonar o repositorio:

```bash
git clone https://github.com/wadson2005/lista_de_tarefas.git
cd lista_de_tarefas
```

- Passo 2: Criar e ativar ambiente virtual:

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- Passo 3: Instalar dependencias:

```bash
pip install -r requirements.txt
```

- Passo 4: Aplicar migracoes:

```bash
python manage.py migrate
```

- Passo 5: Executar servidor:

```bash
python manage.py runserver
```

- Passo 6: Acessar no navegador:

```text
http://127.0.0.1:8000/
```

## Rotas principais

- `/` : lista tarefas e cria nova tarefa
- `/complete/<task_id>/` : marca tarefa como concluida
- `/delete/<task_id>/` : confirma e exclui tarefa
- `/admin/` : painel administrativo Django

## Estrutura do projeto

```text
task/                 # Configuracoes do projeto Django
todo/                 # App principal (models, views, forms, urls)
todo/templates/todo/  # Templates HTML
db.sqlite3            # Banco de dados local
manage.py             # Comandos de execucao e administracao
```

## Modelo de dados

`Task`

- `title` (CharField)
- `completed` (BooleanField)

## Observacoes

- O arquivo `requirements.txt` ja inclui as dependencias do projeto.
- Para ambiente de desenvolvimento, `DEBUG=True` em `task/settings.py`.
