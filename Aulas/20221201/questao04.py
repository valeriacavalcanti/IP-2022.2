import tempo

total = 0

h,m,s = input("Natação: ").split(':')
h,m,s = int(h), int(m), int(s)
total += tempo.converter_para_segundos(h,m,s)

h,m,s = input("Ciclismo: ").split(':')
h,m,s = int(h), int(m), int(s)
total += tempo.converter_para_segundos(h,m,s)

h,m,s = input("Corrida: ").split(':')
h,m,s = int(h), int(m), int(s)
total += tempo.converter_para_segundos(h,m,s)

print(total)
lista = tempo.converter_para_hms(total)
print(lista[0],lista[1],lista[2],sep=':')
