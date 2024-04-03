capacidade_atual, aumento_percentual = map(int, input().split())

valor_atual = int(capacidade_atual*(1+aumento_percentual/100))

print(valor_atual)