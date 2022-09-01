valor_inicial = float(input("Valor inicial: "))
valor_final = float(input("Valor final: "))

if (valor_inicial == valor_final):
    print("valor não alterado")
else:
    if (valor_inicial < valor_final):
        print("Aumento")
        dif = valor_final - valor_inicial
    else:
        print("Desconto")
        dif = valor_inicial - valor_final

    porcentagem = 100 * dif / valor_inicial
    print(porcentagem, "%")
