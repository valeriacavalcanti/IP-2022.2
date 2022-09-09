maior = int(input("Número: "))

for i in range(9): # 0 1 2 3 4 ... 9
    numero = int(input("Número: "))
    if (numero > maior):
        maior = numero

print(maior)
