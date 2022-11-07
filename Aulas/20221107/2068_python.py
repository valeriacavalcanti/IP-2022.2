qtde = 0

while True:
    # obter vários nomes, para quando encontrar "fim"
    nome = input()

    # converter maiúsculo
    nome_maiusculo = nome.upper()

    # verificar se é FIM
    if (nome_maiusculo == "FIM"):
        break

    # calcular a quantidade letras inéditas
    lista = []
    for i in range(len(nome_maiusculo)):
        if (nome_maiusculo[i] >= 'A') and (nome_maiusculo[i] <= 'Z'):
            # verificar se a letra maiúscula é inédita
            if (nome_maiusculo[i] not in lista):
                lista.append(nome_maiusculo[i])

    # auditoria
    # print(len(lista), lista)

    # verificar se o nome possui > 10 letras inéditas -> ++
    if (len(lista) > 10):
        qtde += 1

# exibir a quantidade de nomes com > de 10 letras diferentes
print(qtde)