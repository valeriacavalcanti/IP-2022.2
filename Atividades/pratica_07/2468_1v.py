numeros = []

num = int(input())
while (num != 0):
    numeros.append(num)
    num = int(input())

ultimo = numeros[len(numeros)-1]

for i in range(len(numeros)-1):
    if (numeros[i] > ultimo):
        print(numeros[i])
