soma = 0
qt = int(input("Quantidade de dígitos: "))

# qt = 3

for i in range(qt): # 0 1 2
    b = int(input("Bit: "))
    soma = soma + (b * (2 ** (qt - 1 - i)))

print(soma)
