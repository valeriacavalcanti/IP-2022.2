n1 = int(input("Lado 1: "))
n2 = int(input("Lado 2: "))
n3 = int(input("Lado 3: "))

if (n1 == n2) and (n2 == n3):
    print("Equilatero")
else:
    if (n1 != n2) and (n1 != n3) and (n2 != n3):
        print("Escaleno")
    else:
        print("Isosceles")
