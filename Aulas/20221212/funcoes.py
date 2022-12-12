import random

def quantidade_divisores(numero):
    qtde = 0
    for i in range(1, numero + 1):
        if (numero % i == 0):
            qtde += 1
    return qtde

def divisores(numero):
    lista = []
    for i in range(1, numero+ 1):
        if (numero % i == 0):
            lista.append(i)
    return lista


def aleatorio(qtde, menor, maior, repeticao = True):
    lista = []
    while (len(lista) < qtde):
        numero = random.randint(menor, maior)
        if (repeticao == True):
            lista.append(numero)
        else:
            if (numero not in lista):
                lista.append(numero)
    return lista
