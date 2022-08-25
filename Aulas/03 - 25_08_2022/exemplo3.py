# 400 -> 320
# 100 -> 100

valor = float(input("Valor da compra: "))

if (valor > 200):
    desconto = valor * 0.2
    valor = valor - desconto

print("Valor final: R$ {:.2f}".format(valor))
