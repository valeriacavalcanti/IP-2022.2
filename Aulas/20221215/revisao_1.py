def hexa(numero):
    letras = 'ABCDEF'
    if numero < 10:
        return numero
    else:
        return letras[numero-10]
    

def decimal_tudo(numero, base):
    lista = []
    if (numero == 0):
        st = '0'
    else:
        st = ''
    while (numero != 0):
        lista.append(numero % base)
        numero = numero // base
    for i in range(len(lista)-1,-1,-1):
        if (lista[i] >= 10):
            st += str(hexa(lista[i]))
        else:
            st += str(lista[i])
    return st


# PROGRAMA PRINCIPAL
#print(bin(41)[2:], decimal_tudo(41,2))
#print(bin(42)[2:], decimal_tudo(42,2))
#print(bin(43)[2:], decimal_tudo(43,2))

#for i in range(100,111):
    #print(bin(i)[2:], decimal_tudo(i,2))
    #print(oct(i)[2:], decimal_tudo(i,8))
    #print(hex(i)[2:], decimal_tudo(i,16))

print("Tabela ascii")
for i in range(32, 128):
    b = decimal_tudo(i,2)
    o = decimal_tudo(i,8)
    h = decimal_tudo(i,16)
    s = chr(i)
    print("{} {} {} {} {}".format(i,b,o,h,s))
