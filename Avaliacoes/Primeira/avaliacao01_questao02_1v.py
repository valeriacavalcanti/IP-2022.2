# solução: Jankly e Cauê

q_abaixo = 0
q_carro = q_moto = q_caminhao = 0

tipo, valor, fipe = input().split()
tipo, valor, fipe = int(tipo), float(valor), float(fipe)

barato = valor

if (tipo == 1):
    q_carro += 1
elif (tipo == 2):
    q_moto += 1
else:
    q_caminhao += 1

if (valor < fipe):
    q_abaixo += 1

for i in range(39):
    tipo, valor, fipe = input().split()
    tipo, valor, fipe = int(tipo), float(valor), float(fipe)

    if (valor < barato):
        barato = valor

    if (tipo == 1):
        q_carro += 1
    elif (tipo == 2):
        q_moto += 1
    else:
        q_caminhao += 1

    if (valor < fipe):
        q_abaixo += 1

print(q_carro, q_moto, q_caminhao)
print(barato)
print(q_abaixo)
