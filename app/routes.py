
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Transacao, Categoria

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    transacoes = Transacao.query.order_by(Transacao.data.desc()).all()

    categorias = Categoria.query.all()
    saldo = 0
    for transacao in transacoes:
        if transacao.tipo == 'receita':
            saldo += transacao.valor
        else:
            saldo -= transacao.valor
    return render_template('index.html', transacoes=transacoes, saldo=saldo, categorias=categorias)

@bp.route('/adicionar', methods=['POST'])
def adicionar():
    tipo = request.form['tipo']
    descricao = request.form['descricao']
    valor = float(request.form['valor'])

    categoria_id = request.form['categoria_id']


    nova_transacao = Transacao(tipo=tipo, descricao=descricao, valor=valor, categoria_id=categoria_id)

    db.session.add(nova_transacao)
    db.session.commit()
    flash('Transação adicionada com sucesso!', 'success')
    return redirect(url_for('main.index'))

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    transacao_para_editar = Transacao.query.get_or_404(id)

    categorias = Categoria.query.all()

    if request.method == 'POST':
        transacao_para_editar.tipo = request.form['tipo']
        transacao_para_editar.descricao = request.form['descricao']
        transacao_para_editar.valor = float(request.form['valor'])

        transacao_para_editar.categoria_id = request.form['categoria_id']

        try:
            db.session.commit()
            flash('Transação atualizada com sucesso!', 'success')
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            flash('Erro ao atualizar a transação.', 'error')

    return render_template('editar_transacao.html', transacao=transacao_para_editar, categorias=categorias)

@bp.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    transacao_para_excluir = Transacao.query.get_or_404(id)
    try:
        db.session.delete(transacao_para_excluir)
        db.session.commit()
        flash('Transação excluída com sucesso!', 'success')
    except:
        db.session.rollback()
        flash('Erro ao excluir a transação.', 'error')
    return redirect(url_for('main.index'))