'''
0 "DT_GERACAO"
1 "HH_GERACAO"
2 "ANO_ELEICAO"
3 "CD_TIPO_ELEICAO"
4 "NM_TIPO_ELEICAO"
5 "CD_ELEICAO"
6 "DS_ELEICAO"
7 "DT_ELEICAO"
8 "DT_POSSE"
9 "SG_UF"
10 "SG_UE"
11 "NM_UE"
12 "CD_CARGO"
13 "DS_CARGO"
14 "QT_VAGAS"
'''

def csv_matriz():
    matriz = []
    arq = open('consulta_vagas_2020_BRASIL.csv', 'r')
    for linha in arq.read().splitlines():
        matriz.append(linha.split(';'))
    arq.close()
    return matriz


def estados(matriz):
    lista = []
    for linha in matriz:
        uf = linha[9].replace('"', '')
        if (uf not in lista):
            lista.append(uf)
    lista.sort()
    return lista

def vereadores(matriz):
    soma = 0
    for i in range(len(matriz)):
        if (matriz[i][13] == '"Vereador"'):
            soma += int(matriz[i][14].replace('"', ''))
    return soma

def vereadores_pb(matriz):
    soma = 0
    for i in range(len(matriz)):
        if (matriz[i][13] == '"Vereador"') and (matriz[i][9] == '"PB"'):
            soma += int(matriz[i][14].replace('"', ''))
    return soma

def vereadores_estado(matriz):
    ufs = estados(matriz)
    lista = [0]*len(ufs)
    for linha in matriz:
        if (linha[13] == '"Vereador"'):
            uf = linha[9].replace('"', '')
            posicao = ufs.index(uf)
            lista[posicao] += int(linha[14].replace('"', ''))
    return ufs, lista

def estado_maior_numero_vereadores(matriz):
    estado, qtdes = vereadores_estado(matriz)
    maior = qtdes[0]
    for i in range(1, len(qtdes)):
        if (qtdes[i] > maior):
            maior = qtdes[i]
    lista = []
    for i in range(len(qtdes)):
        if (qtdes[i] == maior):
            lista.append(estado[i])
    return lista

def estado_menor_numero_vereadores(matriz):
    estado, qtdes = vereadores_estado(matriz)
    menor = qtdes[0]
    for i in range(1, len(qtdes)):
        if (qtdes[i] < menor):
            menor = qtdes[i]
    lista = []
    for i in range(len(qtdes)):
        if (qtdes[i] == menor):
            lista.append(estado[i])
    return lista

def municipios(matriz, estado):
    lista = []
    for i in range(len(matriz)):
        if (matriz[i][9].replace('"', '') == estado):
            cidade = matriz[i][11].replace('"', '')
            if (cidade not in lista):
                lista.append(cidade)
    lista.sort()
    return lista
