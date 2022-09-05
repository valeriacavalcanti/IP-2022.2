qt_divisores = 0

n = int(input("Número: "))

# contar os divisores de "n"
for i in range(1, n + 1):
    if (n % i == 0):
        qt_divisores = qt_divisores + 1

# exibir a quantidade de divisores de "n"
print(qt_divisores)


# exibir os múltiplos de "n" que estão entre [10,40]
for i in range(10, 41):
    if (i % n == 0):
        print(i)
