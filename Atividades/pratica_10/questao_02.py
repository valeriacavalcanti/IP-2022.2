# calcular a quantidade de divisores de um número
def divisores(numero):
    qtde = 0
    for i in range(1, numero + 1): # 1 2 3 4 5 6
        if (numero % i == 0):
            qtde += 1
    return qtde

def multiplos(numero):
    qtde = 0
    for i in range(10,41):
        if (i % numero == 0):
            qtde += 1
            # print(i)
    return qtde

def multiplos2(numero):
    lista = []
    for i in range(10,41):
        if (i % numero == 0):
            lista.append(i)
    return lista

# programa principal

num = int(input('Número: '))
print('Quantidade divisores:', divisores(num))
print('Quantidade multiplos:', multiplos(num))
multiplos_10_40 = multiplos2(num)
print('Múltiplos:', multiplos_10_40)
for i in range(len(multiplos_10_40)):
    print(multiplos_10_40[i])
