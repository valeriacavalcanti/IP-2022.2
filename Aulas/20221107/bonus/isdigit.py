# Código da "Prática 09"

# Função "isdigit" de Python

texto = input("Informe um texto: ")

apenas_digitos = True
for i in range(len(texto)):
    if (texto[i] < '0') or (texto[i] > '9'):
        apenas_digitos = False
        break

if (apenas_digitos == True) and (len(texto) > 0):
    print(True)
else:
    print(False)
print(texto.isdigit())
