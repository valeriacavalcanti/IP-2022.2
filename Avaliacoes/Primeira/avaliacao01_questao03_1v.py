q_caixas = 0
soma_peso = 0
maior = 0

peso = float(input())
while (peso != 0):
    q_caixas += 1
    soma_peso += peso

    if (peso > maior):
        maior = peso

    peso = float(input())

print(q_caixas)
if (q_caixas > 0):
    media = soma_peso / q_caixas
    print(media)
    print(maior)
else:
    print('sem media e sem maior')
