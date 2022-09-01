valor = float(input("Valor da compra: "))
cupons = int(valor // 20)
resto = valor - (cupons * 20)

print(cupons, "cupons")

if (resto > 0):
    print("Faltam R$ {:.2f} para novo cupom".format(20 - resto))
