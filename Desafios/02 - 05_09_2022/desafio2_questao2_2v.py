soma = 0
qt = int(input("Quantidade de dígitos: "))

# qt = 3

for i in range(qt - 1, -1, -1): # range(2, -1, -1) = 2 1 0
    b = int(input("Bit: "))
    soma = soma + (b * (2 ** i))

print(soma)
