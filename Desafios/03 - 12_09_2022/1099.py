soma = 0

n = int(input())
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)

    if (x > y):
        x, y = y, x

    soma = 0
    for j in range(x + 1, y):
        if (j % 2 == 1):
            soma = soma + j
    print(soma)
