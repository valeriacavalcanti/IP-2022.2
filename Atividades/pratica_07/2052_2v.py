numeros = []

num = int(input())

while (num not in numeros):
    numeros.append(num)
    num = int(input())

for e in numeros:
    print(e)
