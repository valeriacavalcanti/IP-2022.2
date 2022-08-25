tempo = int(input("Digite o tempo(s): "))

# calcular as hora
horas = tempo // 3600

# atualizar dos segundos, que não formou horas
tempo = tempo % 3600

# calcular os minutos
minutos = tempo // 60

# calcular os segundos
segundos = tempo % 60

print(horas, minutos, segundos, sep=':')
