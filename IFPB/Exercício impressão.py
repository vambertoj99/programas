paginas = int(input())

porcentagem = float(input())

total = int(100*paginas/porcentagem)

print(f"O documento possui {total}")
print(f"Já foram impressas {paginas} paginas")
print(f"Faltam {total - paginas} paginas")