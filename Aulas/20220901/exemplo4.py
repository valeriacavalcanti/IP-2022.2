soma = 0
quantidade = int(input("Quantidade: "))

# repetir n vezes
for i in range(quantidade):
    numero = int(input("Número: "))
    soma = soma + numero

print("Soma =", soma)
