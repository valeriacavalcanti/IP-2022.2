soma = 0
numeros = [0,0,0,0,0,0]

for i in range(6): # 0 1 2 3 4 5
    numeros[i] = int(input("{}º número: ".format(i + 1)))
    soma = soma + numeros[i]

media = soma / 6
print(media)


# quantidade de números com valor acima da média

if (num > media):
    print("maior")
else:
    print("não maior")
