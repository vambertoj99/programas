dias = int(input())

quilometragem = int(input())

diaria = 30*dias
valor_km = 0.01*quilometragem

total = (diaria+valor_km)*0.9

print(f"{total:.2f}")
