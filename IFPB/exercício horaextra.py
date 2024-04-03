salario = float(input())
horas_extras = int(input()) 
custo_hora = salario/44
valor = horas_extras*custo_hora

print(f" {salario + (valor)*1.1:.2f}")