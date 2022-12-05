arq = open("agenda.txt", "a")

for i in range(4):
    nome = input("Nome: ")
    email = input("e-mail: ")
    arq.write("{};{}\n".format(nome, email))

arq.close()

arq = open("agenda.txt", "r")
for linha in arq.read().splitlines():
    nome, email = linha.split(';')
    print(nome)
    print(email)

arq.close()
