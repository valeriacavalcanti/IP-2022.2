# ler 6 números, exibir a quantidade de positivos digitados

qtde = 0

for i in range(6):
    idade = int(input("{} idade:".format(i + 1)))
    if (idade > 0):
        qtde = qtde + 1

print("Quantidade:", qtde)
