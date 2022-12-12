def retorna_dois_valores():
    return 10, 20

def retorna_duas_lista():
    return [10,20], [30, 40]

## PROGRAMA PRINCIPAL

n1, n2 = retorna_dois_valores()
print(n1, n2)

tupla = retorna_duas_lista()
l1, l2 = tupla
print(tupla)
print(l1, l2)
print(tupla[0], tupla[1])
