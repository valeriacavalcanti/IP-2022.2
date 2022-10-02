'''
  Ler 3 notas válidas no suap.
  - [0,100]
  Exibir a média das notas válidas.

  Autor: Júlio Cezar
'''

soma = 0
for i in range(3):
    nota = int(input("Nota: "))
    while (nota < 0) or (nota > 100):
        nota = int(input("Nota: "))
    soma = soma + nota

media = soma // 3
print("Média =", media)

'''
100
200
300
400
-100
80
0

-> 60
'''
