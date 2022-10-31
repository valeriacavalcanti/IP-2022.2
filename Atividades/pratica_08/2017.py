lista = []
maior = -1

for i in range(10):
    texto = input()
    lista.append(texto)
    if (len(texto) > maior):
        maior = len(texto)

print(maior)

for i in range(10):
    if (len(lista[i]) == maior):
        print(lista[i])