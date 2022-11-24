import funcoes

qtde = 0

for i in range(10):
    numero = int(input("Número: "))
    if (funcoes.eh_par(numero) == True):
        qtde += 1

print(qtde)
