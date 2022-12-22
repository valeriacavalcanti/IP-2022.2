estacionamento = []
lotado = qt = erro = 0

for i in range(200):
    mov, placa = input("Movimentação e placa").split()

    if (mov == '1'): # entrada
        if (len(estacionamento) < 8):
            estacionamento.append(placa)
            qt += 1
        else:
            lotado += 1
    else: # saída
        if (placa in estacionamento):
            estacionamento.remove(placa)
        else:
            erro += 1

print(lotado)
print(qt * 4)
print(erro)
