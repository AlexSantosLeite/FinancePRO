# Arquivo: app/models.py

from flask_sqlalchemy import SQLAlchemy
import datetime

# Criamos a instância do SQLAlchemy aqui, para poder usá-la no modelo
db = SQLAlchemy()

class Transacao(db.Model):
    # __tablename__ diz ao SQLAlchemy qual o nome da tabela no banco de dados
    __tablename__ = 'transacoes'

    # Abaixo, definimos as colunas da nossa tabela
    id = db.Column(db.Integer, primary_key=True) # ID único para cada transação
    tipo = db.Column(db.String(7), nullable=False)      # 'receita' ou 'despesa'
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.datetime.now) # Data e hora automáticas

    # Esta função __repr__ é opcional, mas ajuda a gente a ver os dados de forma legível no terminal
    def __repr__(self):
        return f"<Transacao {self.id}: {self.descricao} - R${self.valor}>"