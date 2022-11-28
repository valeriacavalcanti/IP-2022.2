import funcoes

numeros = [0] * 6

for i in range(6):
    numeros[i] = int(input("Número: "))

# qtde números pares
print('Quantidade de pares:', funcoes.quantidade_pares(numeros))

# qtde números positivos
print('Quantidade positivos:', funcoes.quantidade_positivos(numeros))

# qtde valores [10,60]
print('Quantidade 10 60:', funcoes.quantidade_10_60(numeros))

# qtde de valores nulos
print('Quantidade nulos:', funcoes.quantidade_nulos(numeros))

# maior
print('Maior:', funcoes.maior(numeros))

# menor
print('Menor:', funcoes.menor(numeros))
