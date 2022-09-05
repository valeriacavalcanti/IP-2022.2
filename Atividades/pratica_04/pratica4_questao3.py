soma = 0
qtde = 20

# ler os tempos e somar
for i in range(qtde):
    tempo = int(input("Tempo em segundos: "))
    soma = soma + tempo

# calcular a média
media = int(soma/qtde)

# converter para hora, minuto e segundo
horas = media // 3600
minutos = (media % 3600) // 60
segundos = (media % 3600) % 60

# exibir
print(horas, minutos, segundos, sep=":")
