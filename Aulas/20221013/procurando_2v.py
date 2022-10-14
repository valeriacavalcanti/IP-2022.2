lista = [10,13,14,17,12,21,30]

num = int(input("Número: "))

for e in lista:
    if (e == num):
        break

if (e == num):
    print("Existe")
else:
    print("Nao existe")
