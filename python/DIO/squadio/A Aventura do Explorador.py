#Desafio: A Aventura do Explorador

# entrada
quantidade_passos = int(input())

if quantidade_passos == 0:
    print("Nenhum passo dado na floresta")
elif quantidade_passos > 0:
    for indice in range(1,quantidade_passos+1):
        if indice == 1:
            print(f"Explorador: {indice} passo")
        else:
            print(f"Explorador: {indice} passos")
     
