n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))

if (n1 > n2):
    print(n1)
else:
    # n1 não é o maior
    if (n2 > n1):
        print(n2)
    else:
        print("Empate")
