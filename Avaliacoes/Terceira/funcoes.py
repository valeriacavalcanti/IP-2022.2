# Calcular o valor do desconto de uma determinada compra.
def desconto(valor, pagamento):
    if pagamento == 1:
        if (valor <= 100):
            d = 5
        elif (valor <= 200):
            d = 10
        elif (valor <= 400):
            d = 15
        else:
            d = 20
    else:
        if (valor <= 100):
            d = 3
        elif (valor <= 200):
            d = 6
        elif (valor <= 400):
            d = 12
        else:
            d = 15
    return (valor * d)/100

# Calcular a quantidade de cupons de uma determinada compra.
def cupons(valor):
    if (valor <= 100):
        return 2
    elif (valor <= 200):
        return 4
    elif (valor <= 400):
        return 6
    else:
        return 8

# Calcular o valor médio das compras.
def media(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total/200

# Calcular valor da maior compra.
def maior(lista):
    valor = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] > valor):
            valor = lista[i]
    return valor

# Calcular a quantidade total de cupons distribuídos.
def total(lista):
    soma = 0
    for i in range(len(lista)):
        soma += cupons(lista[i])
    return soma

# Iniciais do nome do cliente em letras maiúsculas.
def senha(nome):
    nome = nome.upper()
    st = ''
    for s in nome.split():
      st += s[0]
    return st

# Calcular o menor valor único entre compras.
def menor(lista):
    lances = []
    for i in range(len(lista)):
        if (lista[i] not in lances):
            lances.append(lista[i])
    qt = [0] * len(lances)
    for i in range(len(lances)):
        qt[i] = lista.count(lances[i])
    unicos = []
    for i in range(len(lances)):
        if (qt[i] == 1):
            unicos.append(lances[i])
    if (len(unicos) > 0):
        unicos.sort()
        return unicos[0]
    else:
        return -1
