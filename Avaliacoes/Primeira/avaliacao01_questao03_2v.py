q_caixas = 0
soma_peso = 0
maior = 0

while (True):
    peso = float(input())

    if (peso == 0):
        break
    
    q_caixas += 1
    soma_peso += peso

    if (peso > maior):
        maior = peso

print(q_caixas)
if (q_caixas > 0):
    media = soma_peso / q_caixas
    print(media)
    print(maior)
else:
    print('sem media e sem maior')
