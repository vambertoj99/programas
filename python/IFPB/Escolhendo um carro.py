espaco = input().upper()[0]

mala = input().upper()[0]

valor = float(input())

motor = float(input())

cambio = input().upper()[0]

count = 0

if espaco == "A" and mala == "G":
    if valor < 100000:
        count += 1
        print(count)
    if motor >= 1.5:
        count += 1
        print(count)
    if cambio == "A":
        count += 1
        print(count)
  
else:
    print("Não compre!")


