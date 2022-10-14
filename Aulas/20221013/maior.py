lista = [4,8,10,7,24,32,5]

# exibir os valores a partir dos índices
for i in range(len(lista)):
    print(i, lista[i])

# exibir os valores
for e in lista:
    print(e)

# qual é o maior valor?
maior = lista[0]

for e in lista:
    if (e > maior):
        maior = e

print(maior)

#qual é a posição do maior valor?
indice_maior = 0
for i in range(len(lista)):
    if (lista[i] > lista[indice_maior]):
        indice_maior = i

print(indice_maior,lista[indice_maior])
