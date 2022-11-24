lista = []

for i in range(4):
    nome = input("Nome: ")

    if nome not in lista:
        lista.append(nome)

print(lista)