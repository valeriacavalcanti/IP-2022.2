memoria = []

for i in range(10):
  num = int(input("Número: "))

  # procurar na memória (lista)
  existe = False
  for j in range(len(memoria)):
    if (memoria[j] == num):
      existe = True
      break

  if (existe == False):
    memoria.append(num)

print(memoria)
print(len(memoria))