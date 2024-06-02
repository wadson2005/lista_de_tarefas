# Projeto de Tarefas (Todo List)

Um projeto simples de lista de tarefas (todo list) utilizando Django.

## Funcionalidades
- Adicionar tarefas
- Excluir tarefas

## Instalação
1. Clone o repositório:

`````sh
    git clone https://github.com/wadson2005/lista_de_tarefas.git
   cd lista_de_tarefas
`````ssh

2. Crie e ative um ambiente virtual:

`````sh
    python -m venv venv
    source venv/bin/activate 
`````sh

 No Windows:

`````sh
    venv\Scripts\activate
`````sh

3. Instale as dependências:

`````sh
    pip install -r requirements.txt
`````sh

4. Aplique as migrações:

`````sh
    python manage.py migrate
`````sh

5. Inicie o servidor:

`````sh
    python manage.py runserver
`````sh

## Uso
• Acesse no navegador: `http://127.0.0.1:8000/`
• Adicione e gerencie suas tarefas.