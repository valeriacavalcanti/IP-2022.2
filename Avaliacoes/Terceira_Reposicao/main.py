import funcoes

qtde = 0
maior = -1
segundo = 0
matriculas = []

for i in range(3):
    input('Nome: ')
    matriculas.append(input('Matricula: '))

codigo = int(input('Código do curso: '))

for i in range(len(matriculas)):
    ano = funcoes.ano(matriculas[i])
    entrada = funcoes.entrada(matriculas[i])
    curso = funcoes.curso(matriculas[i])
    sequencia = funcoes.ordem(matriculas[i])

    if (curso == codigo):
        qtde += 1
        if (ano == 2022):
            print(matriculas[i])
        if (ano == 2021) and (sequencia > maior):
            maior = sequencia
    if (entrada == 2) and (ano == 2022):
        segundo += 1

print(qtde)
print(maior)
print(segundo)
