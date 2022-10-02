par = 0
impar = 0
positivo = negativo = 0

for i in range(5):
    n = int(input())

    # verificar par/impar
    if (n % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

    # verificar positivo/negativo
    if (n > 0):
        positivo = positivo + 1
    elif (n < 0):
        negativo = negativo + 1

print(par, 'valor(es) par(es)')
print(impar, 'valor(es) impar(es)')
print(positivo, 'valor(es) positivo(s)')
print(negativo, 'valor(es) negativo(s)')
