import random

m = []

for i in range(4):
    m.append([])
    for j in range(6):
        m[i].append(random.randint(0,1))

for i in range(4):
    print(m[i])

i, j = input("Linha e Coluna: ").split()
i, j = int(i), int(j)

# esquerda
if (j - 1 >= 0) and (m[i][j-1] == 1):
    print("Esquerda", i, j-1)

# direita
if (j + 1 < 6) and (m[i][j+1] == 1):
    print("Direita", i, j + 1)

# acima
if (i - 1 >= 0) and (m[i-1][j] == 1):
    print("Acima", i-1, j)

# abaixo
if (i + 1 < 4) and (m[i+1][j] == 1):
    print("Abaixo", i + 1, j)