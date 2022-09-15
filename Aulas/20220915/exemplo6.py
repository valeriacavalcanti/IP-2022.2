# Tipo 01 - condição no while

qtde = 0

nota = int(input("Nota: "))
while ((nota < 0) or (nota > 100)):
	print("Tá errada!")
	qtde = qtde + 1
	nota = int(input("Nota: "))

print("Nota:", nota)
print("Quantidade de notas inválidas:", qtde)