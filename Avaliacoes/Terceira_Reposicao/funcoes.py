# Retornar o ano da matrícula.
def ano(matricula):
    return int(matricula[:4])

# Retornar a entrada da matrícula
def entrada(matricula):
    return int(matricula[4])

# Retornar o código do curso.
def curso(matricula):
    return int(matricula[5:7])

# Retornar a sequência da matrícula.
def ordem(matricula):
    return int(matricula[7:])

# Calcular a quantidade de matrículas de um determinado curso.
def matriculas(lista, codigo):
    qtde = 0
    for i in range(len(lista)):
        if (curso(lista[i]) == codigo):
            qtde += 1
    return qtde

# Calcular a maior sequência encontrada para um curso em um determinado ano.
def maior(lista, codigo, ano):
    maior = -1
    for i in range(len(lista)):
        if (curso(lista[i]) == codigo) and (ano(lista[i]) == ano):
            if (ordem(lista[i]) > maior):
                maior = ordem(lista[i])
    return maior
