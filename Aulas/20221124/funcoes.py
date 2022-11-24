# funcao para verificar se um número é par
def eh_par(num):
    if (num % 2 == 0):
        return True
    else:
        return False

# função verificar se um símbolo eh vogal
def eh_vogal(simbolo):
    vogais = "aieou".upper()
    if (simbolo.upper() in vogais):
        return True
    else:
        return False

# função para contar as vogais de uma string
def contar_vogais(st):
    qtde = 0
    for i in range(len(st)):
        if (eh_vogal(st[i]) == True):
            qtde += 1

    return qtde

# função para verificar se um número e múltiplo de outro
def multiplo(num1, num2):
    if (num1 % num2 == 0):
        return True
    else:
        return False

# função para retornar o último valor da lista
def ultimo(lista):
    indice = len(lista) - 1
    return lista[indice]

# função para contar os valores da lista múltiplos do último
def contar_multiplos(lista):
    qtde = 0
    valor = ultimo(lista)
    for i in range(len(lista) - 1):
        if (multiplo(lista[i], valor) == True):
            qtde += 1

    return qtde
