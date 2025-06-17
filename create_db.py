
from app import create_app
from app.models import db, Categoria

def seed_data(app):
    with app.app_context():
        print("Verificando e adicionando categorias padrão...")
        categorias_padrao = ['Salário', 'Alimentação', 'Transporte', 'Moradia', 'Lazer', 'Outros']
        for nome_cat in categorias_padrao:
          
            cat = Categoria.query.filter_by(nome=nome_cat).first()
            if not cat:
          
                nova_cat = Categoria(nome=nome_cat)
                db.session.add(nova_cat)
        db.session.commit()
        print("Categorias padrão verificadas/adicionadas.")


print("Iniciando a criação do banco de dados...")
app = create_app()
with app.app_context():
    db.create_all()
print("Banco de dados e tabelas criados com sucesso!")

seed_data(app)