lista = [10,13,14,17,12,21,30]

num = int(input("Número: "))
existe = False

for e in lista:
    if (e == num):
        existe = True
        break

if (existe == True):
    print("Existe")
else:
    print("Nao existe")
