n1 = int(input("Primeiro: "))
n2 = int(input("Segundo: "))
n3 = int(input("Terceiro: "))

if (n2 - n1 == n3 - n2):
    r = n2 - n1
    print("PA", n3 + r)
else:
    r = n2 // n1
    print("PG", n3 * r)
