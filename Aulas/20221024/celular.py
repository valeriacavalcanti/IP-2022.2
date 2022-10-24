import random

# alocar a matriz de toques (tela)
tela = []
for i in range(11):
    tela.append([0]*7)

# gerar os toques aleatórios na tela
for i in range(400):
    l = random.randint(0,10)
    c = random.randint(0,6)
    tela[l][c] += 1

# exibir a matriz de toques (tela)
for i in range(11):
    print(tela[i])

# quantidade de regiões não tocadas
qtde = 0
for i in range(11):
    for j in range(7):
        if (tela[i][j] == 0):
            qtde += 1
print('Não tocadas:',qtde)

# Maior quantidade de toques registrados
# em uma região
maior = tela[0][0]

for i in range(11):
    for j in range(7):
        if (tela[i][j] > maior):
            maior = tela[i][j]
print('Maior:',maior)

# qual(is) região(ões) onde houve o maior
# número de toques
print("região(ões) com maior toque")
for i in range(11):
    for j in range(7):
        if (tela[i][j] == maior):
            print(i, j)