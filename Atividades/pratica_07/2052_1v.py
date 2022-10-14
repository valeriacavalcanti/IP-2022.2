numeros = []

num = int(input())
existe = False

while (existe == False):
    numeros.append(num)
    num = int(input())

    # verificar se nao esta na lista
    for e in numeros:
        if (e == num):
            existe = True
            break

for e in numeros:
    print(e)
