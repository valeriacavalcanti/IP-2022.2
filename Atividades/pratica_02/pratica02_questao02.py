descricao = input("Descrição: ")    # Chocolate
valor = float(input("Valor: "))     # 10

desconto = valor * 0.2              # 2
valor = valor - desconto            # 8

print("Descrição = {} - Desconto = {} - Valor final = {:.2f}".format(descricao, desconto, valor))
