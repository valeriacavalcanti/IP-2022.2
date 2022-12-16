def tudo_decimal(numero, base):
    mp = len(numero) - 1
    soma = 0
    for i in range(len(numero)):
        if (numero[i] in 'ABCDEF'):
            valor = 'ABCDEF'.index(numero[i])+10
        else:
            valor = int(numero[i])
        soma += valor * base ** (mp-i)
    return soma


# PROGRAMA PRINCIPAL

# 122 124 127

print(int('1111010',2), tudo_decimal('1111010',2))
print(int('1111100',2), tudo_decimal('1111100',2))
print(int('1111111',2), tudo_decimal('1111111',2))

#print(int('172',8), tudo_decimal('172',8))
#print(int('174',8), tudo_decimal('174',8))
#print(int('177',8), tudo_decimal('177',8))

#print(int('7A',16), tudo_decimal('7A',16))
#print(int('7C',16), tudo_decimal('7C',16))
#print(int('7F',16), tudo_decimal('7F',16))
