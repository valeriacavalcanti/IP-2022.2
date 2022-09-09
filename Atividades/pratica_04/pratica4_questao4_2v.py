maior = 0

for i in range(10): # 0 1 2 3 4 ... 9
    numero = int(input("Número: "))
    
    if (i == 0):
        maior = numero
    else:
        if (numero > maior):
            maior = numero

print(maior)
