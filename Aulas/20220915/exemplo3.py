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
print("Soma:",soma)
