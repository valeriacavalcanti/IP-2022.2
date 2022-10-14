numeros = []
ultimo = 0

while(True):
    num = int(input())

    if (num == 0):
        break

    ultimo = num
    numeros.append(num)

for e in numeros:
    if (e > ultimo):
        print(e)
