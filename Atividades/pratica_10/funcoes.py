# retornar se um número é par
def par(numero):
    if (numero % 2 == 0):
        return True
    else:
        return False

# retornar se um número é positivo
def positivo(numero):
    return (numero > 0)

# retorna quantidade de números pares
def quantidade_pares(lista):
    qtde = 0

    for i in range(len(lista)):
        if (par(lista[i]) == True):
            qtde += 1

    return qtde

# retorna quantidade de números positivos
def quantidade_positivos(lista):
    qtde = 0

    for i in range(len(lista)):
        if (positivo(lista[i])):
            qtde += 1
    return qtde

# retorna quantidade de valores entre 10 e 60
def quantidade_10_60(lista):
    qtde = 0

    for i in range(len(lista)):
        if (lista[i] >= 10) and (lista[i] <= 60):
            qtde += 1

    return qtde

# retorna quantidade de valores nulos
def quantidade_nulos(lista):
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] == 0):
            qtde += 1
    return qtde

# retorna o maior valor da lista
def maior(lista):
    maior_valor = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] > maior_valor):
            maior_valor = lista[i]
    return maior_valor

# retorna o menor valor da lista
def menor(lista):
    menor_valor = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] < menor_valor):
            menor_valor = lista[i]
    return menor_valor
