import funcoes

# print(funcoes.quantidade_divisores(11))
# print(funcoes.quantidade_divisores(12))

# print(funcoes.quantidade_divisores(15))
# print(funcoes.divisores(15))

lista_com_repeticao = funcoes.aleatorio(5,1,5)
lista_sem_repeticao = funcoes.aleatorio(5,1,5, False)
print(lista_com_repeticao)
print(lista_sem_repeticao)

print(lista_com_repeticao.count(5))

print('valeria'.count('a'))
print('valeria'.count('a', 3))
print('valeria'.count('a', 2, 4))
