import funcoes

numeros = [0] * 10
for i in range(10):
    numeros[i] = int(input("Número: "))

print(funcoes.contar_multiplos(numeros))
