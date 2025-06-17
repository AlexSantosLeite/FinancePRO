# Arquivo: app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
# Importamos nosso modelo de Transacao e o objeto db
from .models import db, Transacao

# Blueprint é a forma do Flask de organizar um grupo de rotas relacionadas
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Busca todas as transações no banco de dados, ordenadas pela mais recente
    transacoes = Transacao.query.order_by(Transacao.data.desc()).all()

    # Calcula o saldo
    saldo = 0
    for transacao in transacoes:
        if transacao.tipo == 'receita':
            saldo += transacao.valor
        else:
            saldo -= transacao.valor

    # render_template vai renderizar o arquivo HTML, passando as variáveis para ele
    return render_template('index.html', transacoes=transacoes, saldo=saldo)

@bp.route('/adicionar', methods=['POST'])
def adicionar():
    # Pega os dados enviados pelo formulário HTML
    tipo = request.form['tipo']
    descricao = request.form['descricao']
    valor = float(request.form['valor'])

    # Cria uma nova instância da Transacao com os dados do formulário
    nova_transacao = Transacao(tipo=tipo, descricao=descricao, valor=valor)

    # Adiciona a nova transação à sessão do banco de dados
    db.session.add(nova_transacao)
    # Confirma a transação, salvando-a permanentemente no banco
    db.session.commit()

    # Redireciona o usuário de volta para a página inicial
    return redirect(url_for('main.index'))

# Adicione este código NO FINAL do arquivo app/routes.py

@bp.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    # .get_or_404() é um atalho útil do Flask-SQLAlchemy:
    # ele tenta encontrar a transação pelo ID. Se não encontrar, ele automaticamente retorna um erro 404 (Página não encontrada).
    transacao_para_excluir = Transacao.query.get_or_404(id)

    try:
        # Marca a transação para ser deletada
        db.session.delete(transacao_para_excluir)
        # Confirma a exclusão, salvando a mudança no banco de dados
        db.session.commit()
        # Se desejar, pode adicionar uma mensagem de sucesso aqui (veremos isso no futuro)
    except:
        # Em caso de erro, desfaz a operação
        db.session.rollback()
        # Poderíamos adicionar uma mensagem de erro aqui
    
    # Independentemente do resultado, redireciona o usuário de volta para a página inicial
    return redirect(url_for('main.index'))