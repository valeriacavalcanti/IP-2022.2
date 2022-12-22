matriz = []
invalido = 0

for i in range(3):
    matriz.append([True] * 6)

for i in range(3):
    matriz.append([False] * 6)

for i in range(2):
    lo, co = input('Origem: ').split()
    lo, co = int(lo), int(co)
    ld, cd = input('Destino: ').split()
    ld, cd = int(ld), int(cd)

    if (matriz[lo][co] == True) and (matriz[ld][cd] == False):
        matriz[lo][co] = False
        matriz[ld][cd] = True
    else:
        invalido += 1

print(invalido)
for i in range(6):
    for j in range(6):
        print(matriz[i][j], end=' ')
    print()
