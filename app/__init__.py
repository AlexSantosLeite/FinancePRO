# Arquivo: app/__init__.py

import os
from flask import Flask
# Importa o objeto 'db' que definimos no arquivo models.py
from .models import db

# Este é um padrão chamado "Application Factory". Ajuda a organizar o projeto.
def create_app():
    # Cria a instância da aplicação Flask
    app = Flask(__name__)

    # Configuração do banco de dados
    # Pega o caminho absoluto da pasta do projeto
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Define o caminho para o arquivo do banco de dados. Ele ficará na pasta principal.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'finance.db')
    # Configuração para desativar um recurso do SQLAlchemy que não usaremos e que consome memória
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Conecta nossa instância 'db' (dos modelos) com a aplicação Flask
    db.init_app(app)

    # Na próxima aula, vamos importar e registrar nossas rotas (páginas) aqui
    from . import routes
    app.register_blueprint(routes.bp)

    return app