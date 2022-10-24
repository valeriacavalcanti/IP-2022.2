# Dúvida de Jonas

import random

aleatorio = random.randint(1,10)

for i in range(5):
    num = int(input("Número: "))
    if (num == aleatorio):
        break

if (num == aleatorio):
    print("acertou!")
else:
    print("errou!")

print(aleatorio)