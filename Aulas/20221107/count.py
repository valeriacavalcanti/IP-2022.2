qtde = 0

texto = input("Texto: ")
simbolo = input("Símbolo: ")
intervalo = input("Intervalo:" ).split()

if (len(intervalo) == 0):
    start = 0
    stop = len(texto)
elif (len(intervalo) == 1):
    start = int(intervalo[0])
    stop = len(texto)
else:
    start = int(intervalo[0])
    stop = int(intervalo[1])
    if (stop > len(texto)):
        stop = len(texto)

# vamos contar!
for i in range(start, stop):
    if (texto[i] == simbolo):
        qtde += 1

print(qtde)

if (len(intervalo) == 0):
    print(texto.count(simbolo))
elif (len(intervalo) == 1):
    print(texto.count(simbolo, int(intervalo[0])))
else:
    print(texto.count(simbolo, int(intervalo[0]), int(intervalo[1])))