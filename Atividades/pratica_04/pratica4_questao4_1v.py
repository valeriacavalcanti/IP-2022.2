maior = 0

for i in range(10): # 0 1 2 3 4 ... 9
    if (i == 0):
        maior = int(input("Número: "))
    else:
        numero = int(input("Número: "))
        if (numero > maior):
            maior = numero

print(maior)
