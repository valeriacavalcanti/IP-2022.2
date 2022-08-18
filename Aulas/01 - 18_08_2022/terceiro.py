# Obter um número, calcular e exibir a soma dos números de 1 até esse número lido.
# https://www.educamaisbrasil.com.br/enem/matematica/progressao-aritmetica


numero = int(input("Digite o número (inteiro positivo): "))

soma = ((1 + numero) * numero)/2
soma = int(soma)

print("A soma de todos os números entre 1 e {} = {}".format(numero, soma))
