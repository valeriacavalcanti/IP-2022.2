q_par = 0
q_positivo = 0
q_intervalo = 0
q_nulo = 0

for i in range(6):
    n = int(input("Número: "))

    # verificar se é par
    if (n != 0) and (n % 2 == 0):
        q_par = q_par + 1

    # verificar se é positivo
    if (n > 0):
        q_positivo = q_positivo + 1

    # verificar se está no intervalo
    # entre [10,60]
    if (n >= 10) and (n <= 60):
        q_intervalo = q_intervalo + 1

    # verificar se é nulo
    if (n == 0):
        q_nulo = q_nulo + 1


# exibir o resultado
print("Pares:", q_par)
print("Positivos", q_positivo)
print("Entre [10,60]:", q_intervalo)
print("Nulos:", q_nulo)
