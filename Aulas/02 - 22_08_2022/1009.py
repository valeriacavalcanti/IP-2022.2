nome = input("Nome: ")
salario_fixo = float(input("Salário: "))
vendas = float(input("Vendas: "))

comissao = vendas * 0.15
salario_final = salario_fixo + comissao

print("TOTAL = R$ {:.2f}".format(salario_final))
