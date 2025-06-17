
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Categoria {self.nome}>"

class Transacao(db.Model):
    __tablename__ = 'transacoes'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(7), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.datetime.now)


    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    categoria = db.relationship('Categoria', backref=db.backref('transacoes', lazy=True))

    def __repr__(self):
        return f"<Transacao {self.id}: {self.descricao} - R${self.valor}>"