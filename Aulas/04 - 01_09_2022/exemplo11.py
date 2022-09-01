# em grupo de 6 pessoas, calcular a média das idades

soma = 0

for i in range(6):
    idade = int(input("{} idade:".format(i + 1)))
    soma = soma + idade

media = soma / 6

print("Média = {:.1f}".format(media))
