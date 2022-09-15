qtde = 0
soma = 0
media = 0

while (True):
    print("eita")
    num = int(input("Número: "))
    if (num == 0):
        break

    # o número NÃO é zero
    qtde = qtde + 1
    soma = soma + num

print("Saiu")
print("Num:",num) # 0 (zero)
print("Qtde:",qtde)
if (qtde > 0):
    print("Soma:",soma)
    media = soma / qtde
    print("Média:", media)
else:
    print("nenhum valor digitado")
