qtde = 0

while True:
    # obter vários nomes, para quando encontrar "fim"
    nome = input()

    # converter maiúsculo
    nome_maiusculo = ""
    for i in range(len(nome)):
        if (nome[i] >= 'a') and (nome[i] <= 'z'):
            nome_maiusculo += chr(ord(nome[i]) - 32)
        else:
            nome_maiusculo += nome[i]

    # verificar se é FIM
    if (nome_maiusculo == "FIM"):
        break

    # calcular a quantidade letras inéditas
    lista = []
    for i in range(len(nome_maiusculo)):
        if (nome_maiusculo[i] >= 'A') and (nome_maiusculo[i] <= 'Z'):
            # verificar se a letra maiúscula é inédita
            existe = False
            for j in range(len(lista)):
                if (lista[j] == nome_maiusculo[i]):
                    existe = True
                    break
            if (existe == False):
                lista.append(nome_maiusculo[i])

    # auditoria
    # print(len(lista), lista)

    # verificar se o nome possui > 10 letras inéditas -> ++
    if (len(lista) > 10):
        qtde += 1

# exibir a quantidade de nomes com > de 10 letras diferentes
print(qtde)