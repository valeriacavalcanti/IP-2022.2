# Carregar os dados do arquivo CSV na matriz
def ler_csv():
    matriz = []
    arq = open('resultados.csv', 'r')
    for r in arq.read().splitlines():
        matriz.append(r.split(';'))
    arq.close()
    return matriz

# [1] Quantas edições da Copa do Mundo já foram realizadas.
def edicoes(matriz):
    return len(matriz)

# [2] Quais países já sediaram a Copa do Mundo?
def sedes(matriz):
    lista = []
    for linha in matriz:
        if (linha[1] not in lista):
            lista.append(linha[1])
    lista.sort() # ordena a lista
    return lista

# [3] Quantas vezes o Brasil já foi campeão?
def brasil_campeao(matriz):
    qtde = 0
    for linha in matriz:
        if (linha[2] == 'Brasil'):
            qtde += 1
    return qtde

# [4] Premiações que o Brasil já recebeu?
def premiacoes_brasil(matriz):
    qtde = 0
    for linha in matriz:
        if ('Brasil' in linha[2:]):
            qtde += 1
    return qtde

# [5] Países que conquistaram o título na Copa do Mundo?
# [6] Países que ficaram em segundo lugar?
# [7] Países que ficaram em terceiro lugar?
# [8] Países que ficaram em quarto lugar?
def titulos(matriz, classificacao):
    lista = []
    for linha in matriz:
        if (linha[classificacao + 1] not in lista):
            lista.append(linha[classificacao + 1])
    lista.sort() # ordena a lista
    return lista

# [9] País(es) que possui(em) a maior quantidade de títulos?
def maior_titulos(matriz):
    paises = []
    titulos = []
    for linha in matriz:
        if (linha[2] not in paises):
            paises.append(linha[2])
            titulos.append(1)
        else:
            titulos[paises.index(linha[2])] += 1
    maior = max(titulos)
    vencedores = []
    for i in range(len(paises)):
        if (titulos[i] == maior):
            vencedores.append(paises[i])
    return vencedores

# [10] País(es) que participaram de uma final da Copa?
def participacao_final(matriz):
    paises = []
    for linha in matriz:
        if (linha[2] not in paises):
            paises.append(linha[2])
        if (linha[3] not in paises):
            paises.append(linha[3])
    paises.sort() # ordena a lista
    return paises
