'''
  Ler 3 notas válidas no suap.
  - [0,100]
  Exibir a média das notas válidas.

  Autor: Lucas Vinícius
'''

qt = 0
soma = 0
while (qt < 3):
    nota = int(input("Nota: "))
    if (nota >= 0) and (nota <= 100):
        qt = qt + 1
        soma = soma + nota

media = soma // 3
print('Média =', media)
print("saiu")


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
