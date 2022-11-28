# retornar o maior dos lados
def maior(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        return n1
    elif (n2 > n3):
        return n2
    else:
        return n3

# validar se as medidas formam triângulo
def validar(n1, n2, n3):
    maior_valor = maior(n1, n2, n3)
    if (n1 > n2) and (n1 > n3):
        soma = n2 + n3
    elif (n2 > n3):
        soma = n1 + n3
    else:
        soma = n1 + n2
    return maior_valor < soma

# validar se as medidas formam triângulo
def validar2(n1, n2, n3):
    maior_valor = maior(n1, n2, n3)
    return maior_valor < (n1 + n2 + n3) - maior_valor

# retornar o tipo de triângulo formado por três medidas
def tipo(n1, n2, n3):
    if (n1 == n2) and (n1 == n3):
        return "EQUILÁTERO"
    elif (n1 != n2) and (n1 != n3) and (n2 != n3):
        return "ESCALENO"
    else:
        return "ISÓSCELES"



# PROGRAMA PRINCIPAL
m1, m2, m3 = input("Medidas:").split()
m1, m2, m3 = int(m1), int(m2), int(m3)

if (validar(m1, m2, m3)):
    print(tipo(m1, m2, m3))
else:
    print("Não forma triângulo!")
