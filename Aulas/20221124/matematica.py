# função para somar os elementos da lista
def somar(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]

    return soma

# função para calcular a média
def media(lista):
    return somar(lista)/len(lista)
