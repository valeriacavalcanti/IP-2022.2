tempo = int(input())

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = (tempo % 3600) % 60

print("{}:{}:{}".format(horas, minutos, segundos))
