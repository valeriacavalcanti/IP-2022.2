soma = 0
qt_abaixo = 0
qt = int(input("Quantidade: "))

numeros = [0] * qt

# ler os números
for i in range(qt):
    numeros[i] = int(input("Número: "))
    soma = soma + numeros[i]

media = soma / qt
print("Soma =", soma)
print("Média =", media)

# exibir TODOS os números
for i in range(qt):
    print(numeros[i])

# exibir os números com valor ACIMA da média
for i in range(qt):
    if (numeros[i] > media):
        print(numeros[i])
    elif (numeros[i] < media):
        qt_abaixo += 1

print(qt_abaixo)
