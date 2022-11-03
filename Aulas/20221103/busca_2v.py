memoria = []

for i in range(10):
  num = int(input("Número: "))

  if num not in memoria:
    memoria.append(num)

print(memoria)
print(len(memoria))