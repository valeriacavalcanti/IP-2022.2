import matematica

# função para somar os elementos da lista
def somar(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]

    return soma

# função para calcular a média
def media(lista):
    return somar(lista)/len(lista)

# programa principal
notas = []
for i in range(10):
    notas.append(int(input("Nota: ")))

print("Média =", media(notas))
print("Média =", matematica.media(notas))
