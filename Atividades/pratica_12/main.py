import tse

dados = tse.csv_matriz()

print('Tamanho:', len(dados))

estados = tse.estados(dados)
print('Estados:', len(estados), estados)

print('Vereadores do Brasil:', tse.vereadores(dados))
print('Vereadores da Paraiba:', tse.vereadores_pb(dados))

estados, qtdes = tse.vereadores_estado(dados)

# print(estados)
# print(qtdes)

for i in range(len(estados)):
    print(estados[i], qtdes[i])

print('Maior:', tse.estado_maior_numero_vereadores(dados))
print('Menor:', tse.estado_menor_numero_vereadores(dados))

print(tse.municipios(dados, 'PB'))
