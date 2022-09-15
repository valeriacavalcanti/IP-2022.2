# Tipo 02 - loop infinito

qtde = 0

while (True):
	nota = int(input("Nota: "))
	if ((nota >= 0) and (nota <= 100)):
		break
	qtde = qtde + 1

print("Nota:", nota)
print("Quantidade de notas inválidas:", qtde)