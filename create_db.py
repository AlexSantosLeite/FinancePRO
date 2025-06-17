# Arquivo: create_db.py
from app import create_app
from app.models import db

print("Iniciando a criação do banco de dados...")

app = create_app()

with app.app_context():
    # O comando db.create_all() olha todos os modelos que definimos
    # e cria as tabelas correspondentes no banco de dados.
    db.create_all()

print("Banco de dados e tabelas criados com sucesso!")