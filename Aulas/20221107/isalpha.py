qtde = 0
texto = input("Texto: ")

for i in range(len(texto)):
    if ((texto[i] >= 'a') and (texto[i] <= 'z')) or ((texto[i] >= 'A') and (texto[i] <= 'Z')):
        qtde += 1

if (len(texto) > 0) and (len(texto) == qtde):
    print(True)
else:
    print(False)

# auditoria
print(texto.isalpha())