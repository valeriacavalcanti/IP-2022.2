# alocar a matriz de lugares
lugares = []
for i in range(5):
    lugares.append([False]*6)

# tentar vender os 10 ingressos
for i in range(10):
    l,c = input("Linha e coluna: ").split()
    l,c = int(l), int(c)
    if (lugares[l][c] == False):
        lugares[l][c] = True

# calcular a quantidade lugares vendidos (True)
qtde = 0
for i in range(5):
    for j in range(6):
        if (lugares[i][j] == True):
            qtde += 1

# exibir a quantidade de ingressos vendidos com sucesso!
print(qtde)