# anote-ai
Sistema Web de Gestão de Tarefas com Autenticação de Usuários - Python ,Django e SQLite


Esta é uma aplicação web de gerenciamento de tarefas (To-Do List) desenvolvida em Django com SQLite. A aplicação permite que os usuários registrem contas, façam login e gerenciem suas próprias listas de tarefas, com funcionalidades para criar, visualizar, atualizar e excluir tarefas, além de marcar tarefas como concluídas ou a fazer.

## Funcionalidades

- Registro de usuários.
- Login/Logout de usuários.
- Gerenciamento de tarefas por cada usuário:
  - Criar novas tarefas (com o status inicial de "a fazer").
  - Visualizar lista de tarefas.
  - Editar e atualizar tarefas.
  - Excluir tarefas.
  - Marcar tarefas como "a fazer" ou "concluídas".

## Requisitos

- Python 3.x
- Django 4.x
- SQLite3 (banco de dados padrão do Django)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/paulocastanha33/anote-ai.git
   cd to-do-list-django
   ```

2. **Crie um ambiente virtual e ative-o:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o painel de administração do Django (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação no navegador:**
   Abra `http://127.0.0.1:8000/` em seu navegador.

## Estrutura do Projeto

```bash
ANOTE-AI/
│
├── anote_ai/               # Aplicação Django principal
│   ├── migrations/         # Arquivos de migração do banco de dados
│   ├── templates/          # Templates HTML
│   ├── models.py           # Modelos de dados (Tarefas e Usuários)
│   ├── views.py            # Lógica das páginas
│   ├── urls.py             # Rotas da aplicação
│   └── forms.py            # Formulários (Tarefas)
│
├── manage.py               # Script de gerenciamento do Django
├── db.sqlite3              # Banco de dados SQLite gerado automaticamente
├── requirements.txt        # Arquivo de dependências
└── README.md               # Documentação do projeto
```

## Como Usar

1. **Registro e Login:**
   - Crie uma conta através da página de registro.
   - Faça login para acessar suas listas de tarefas.

2. **Gerenciar Tarefas:**
   - Crie novas tarefas através da interface de criação.
   - Marque tarefas como "a fazer" ou "concluídas" usando os botões apropriados.
   - Atualize as informações de uma tarefa ou exclua uma tarefa quando desejar.

## Tecnologias Utilizadas

- **Django**: Framework web Python para a construção da aplicação.
- **SQLite**: Banco de dados embutido usado para armazenamento local.
- **HTML/CSS**: Usado para a interface do usuário.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---

Esse README fornece uma descrição clara do projeto, instruções de instalação, uso e contribuições, além de informações sobre as funcionalidades e a estrutura do código.
