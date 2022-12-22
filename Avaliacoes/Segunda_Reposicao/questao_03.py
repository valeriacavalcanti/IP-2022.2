frase = input('Frase: ')
inverte = ''

for i in range(len(frase)):
    if (frase[i] >= 'A') and (frase[i] <= 'Z'):
        inverte += chr(ord(frase[i]) + 32)
    elif (frase[i] >= 'a') and (frase[i] <= 'z'):
        inverte += chr(ord(frase[i]) - 32)
    else:
        inverte += frase[i]

print(inverte)
