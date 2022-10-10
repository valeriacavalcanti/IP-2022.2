# solução: Lucas Vinícius

q_abaixo = 0
q_carro = q_moto = q_caminhao = 0

for i in range(40):
    tipo, valor, fipe = input().split()
    tipo, valor, fipe = int(tipo), float(valor), float(fipe)

    if (i == 0) or (valor < barato):
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
