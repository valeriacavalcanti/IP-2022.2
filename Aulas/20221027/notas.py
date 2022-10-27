qt = 2
notas = []
for i in range(qt):
  notas.append([0]*3)

for i in range(qt):
  print("Aluno:", i + 1)
  for j in range(3):
    notas[i][j] = int(input("Nota {}:".format(j + 1)))

for i in range(qt):
  print(notas[i])