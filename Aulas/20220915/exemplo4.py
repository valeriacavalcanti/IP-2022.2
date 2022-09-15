qtde = 0
soma = 0

num = int(input("Número: "))
while (num != 0):
    qtde = qtde + 1
    soma = soma + num
    num = int(input("Número: "))

print("Saiu")
print("Num:",num) # 0 (zero)
print("Qtde:",qtde)
if (qtde > 0):
    print("Soma:",soma)
    media = soma / qtde
    print("Média:", media)
else:
    print("nenhum valor digitado")
