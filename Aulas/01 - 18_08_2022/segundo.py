# Obter três notas, calcular e exibir a média aritmética e a média ponderada.
# Pesos: nota 1 (20), nota 2 (20) e nota 3 (40).


nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

media_aritmetica = (nota1 + nota2 + nota3) / 3
media_ponderada = (nota1 * 20 + nota2 * 20 + nota3 * 40)/80

print("Média aritmética = {:.2f}".format(media_aritmetica))
print("Média ponderada = {:.2f}".format(media_ponderada))
