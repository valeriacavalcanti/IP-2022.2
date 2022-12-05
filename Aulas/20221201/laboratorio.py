# criar arquivo
#arq = open("dados.txt", "w")
# w - criar/recriar

# abrir arquivo
arq = open("dados.txt", "r")
# r - leitura
# a - append (cria/abre) para escrita

# escrever no arquivo
#frase = input("Frase: ")
#arq.write(frase + '\n')

# ler o que está no arquivo
#texto = arq.read()
# print(texto)

#lista = arq.readlines()
#for linha in lista:
#    print(linha)

lista = arq.read().splitlines()
for linha in lista:
    print(linha)

# fechar arquivo
arq.close()

print("tudo certo")
