valor = float(input("Valor: "))
desconto = 0

if (valor <= 100):
    desconto = valor * 0.1
elif (valor <= 200):
    desconto = valor * 0.15
else:
    desconto = valor * 0.2

print(valor - desconto)
