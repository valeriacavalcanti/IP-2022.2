n1, n2 = input("Digite dois valores: ").split()
n1, n2 = int(n1), int(n2)

if (n1 > n2):
    temp = n1
    n1 = n2
    n2 = temp

print(n1, n2)
