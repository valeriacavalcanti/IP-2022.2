qtde = 0
texto = input("Texto: ")

for i in range(len(texto)):
    if (texto[i] >= '0') and (texto[i] <= '9'):
        qtde += 1

if (len(texto) > 0) and (len(texto) == qtde):
    print(True)
else:
    print(False)

# auditoria
print(texto.isdigit())