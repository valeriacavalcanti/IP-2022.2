modelo = []
custo = []
lucro = []
qtde = []
maior = -1

for i in range(4):
  modelo.append(input("Modelo: "))
  custo.append(float(input("Custo: ")))
  lucro.append(float(input("Lucro: ")))
  qtde.append(int(input("Quantidade: ")))


# valor final
for i in range(4):
  valor = custo[i] + lucro[i]
  if (valor > maior):
    maior = valor
  print("{} - R$ {:.2f}".format(modelo[i], valor))

# lucro total com a venda de todos os veículos
soma = 0
for i in range(4):
  soma = soma + (lucro[i] * qtde[i])

print("Soma:", soma)

# média do lucro arrecadado com a venda de todos os veículos
media = soma / sum(qtde)
print("Média:", media)

# descobrir maior valor a partir do primeiro (jonas)
maior = custo[0] + lucro[0]
for i in range(1,4):
  if (custo[i] + lucro[i] > maior):
    maior = custo[i] + lucro[i]

# exibir o(s) modelo(s) mais caro(s)
print("Valor mais caro:", maior)

print("Modelo(s) mais caro(s):")
for i in range(4):
  if (custo[i] + lucro[i] == maior):
    print(modelo[i])