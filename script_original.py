import csv
from datetime import datetime


def salvar_transacao(tipo, valor):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("transacoes.csv", "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([tipo, valor, data_hora])
        
def carregar_saldo():
    saldo = 0
    try:
        with open("transacoes.csv", "r") as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if len(linha) == 3:
                    tipo, valor, _ = linha
                    try:
                        
                        valor = float(valor)
                        if tipo == "Entrada":
                            saldo += valor
                        elif tipo == "Saída":
                            saldo -= valor
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass
    return saldo
        
def mostrar_historico():
    try:
        with open("transacoes.csv", "r") as arquivo:
            reader = csv.reader(arquivo)
            print("\n=== HISTÓRICO DE TRANSAÇÕES ===")
            for linha in reader:
                if len(linha) == 3:
                    tipo, valor, data = linha
                    print(f"{data} | {tipo}: R${valor}")
    except FileNotFoundError:
        print("Nenhuma transação registrada ainda.")
        
saldo = carregar_saldo()
        
while True:
    print("=== CONTREOLE FINANCEIRO ===")
    print("1. Adicionar entrada")
    print("2. Adicionar saída")
    print("3. ver saldo atual")
    print("4. Ver histórico de transações")
    print("5. Sair")
    
    opçao = input("Digite o número para operação: ")
    
    if opçao == "1":
        
        deposito = float(input("Digite o valor para depósito: "))
        
        saldo += deposito
        salvar_transacao("Entrada", deposito)
        
    elif opçao == "2":
        
        retirada = float(input("Digite o valor para retirada: "))
        if retirada > saldo:
            
            print("Saldo insulficiente!")
            
        else:
            
            saldo -= retirada
            salvar_transacao("Saída", retirada)
            
            print(f"Você retirou R${retirada}")
            print(f"Saldo atual R${saldo}")
            
    elif opçao == "3":
        
        print(f"Seu saldo atual é R${saldo}")
    
    elif opçao == "4":
        
       mostrar_historico()
    
    elif opçao == "5":
        
        print("Saindo do sistema...")
        break
    
    else:
        
        print("Opção inválida. Tente novamente.")