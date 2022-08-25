valor = float(input("Valor: "))
desconto = 0

if (valor <= 100):
    desconto = valor * 0.1

if (valor > 100) and (valor <= 200):
    desconto = valor * 0.15

if (valor > 200):
    desconto = valor * 0.2

print(valor - desconto)
