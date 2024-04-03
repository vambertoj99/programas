saldo = 0
limite_saque = 3
extrato = []
menu = """
Bem Vindo ao Banco BANCO

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> Digite a opção correspondente: """

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor < 0:
            print("Digite um valor válido.")
        else:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
                            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if valor < 0:
            print("Digite um valor Válido")
        
        elif limite_saque == 0:
            print("Operação falhou: Limite de três saques diário.")
        
        elif valor > 500:
            print("Operação falhou: Limite por saque é de R$ 500.00")
        
        elif valor > saldo:
            print("Operação falhou: O saldo não é suficiente para a operação.")
        
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            limite_saque -= 1
        
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato == []:
            print("\nNão foram realizadas movimentações.")
        else:
            for item in extrato:
                print(item)
            print(f"\nSaldo = R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == "q":
        print("Saindo...")
        print("O banco BANCO agradece seu contato!")
        break
    
    else:
        print("Opção inválida! Digite a letra correspondente!")

