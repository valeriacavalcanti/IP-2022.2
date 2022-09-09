soma = 0
qt = int(input("Quantidade de dígitos: "))

for i in range(qt, 0, -1):
    b = int(input("Bit: "))
    soma = soma + (b * (2 ** (i - 1)))

print(soma)
