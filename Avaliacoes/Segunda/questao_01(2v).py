lista = []

for i in range(4):
    nome = input("Nome: ")
    existe = False
    for j in range(len(lista)):
        if (nome == lista[j]):
            existe = True
            break

    if (existe == False):
        lista.append(nome)

print(lista)