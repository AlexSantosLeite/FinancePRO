# Arquivo: run.py

from app import create_app

# Cria a aplicação usando a nossa factory function
app = create_app()

# A linha abaixo garante que o servidor só vai rodar se executarmos este arquivo diretamente
if __name__ == '__main__':
    # app.run() inicia o servidor web do Flask
    # debug=True é ótimo para desenvolvimento: o servidor reinicia sozinho quando você salva uma alteração no código.
    app.run(debug=True)