qa = qe = qi = qo = qu = 0

for i in range(10):
    frase = input()
    for j in range(len(frase)):
        if (frase[j] == 'A') or (frase[j] == 'a'):
            qa += 1
        elif (frase[j] == 'E') or (frase[j] == 'e'):
            qe += 1
        elif (frase[j] == 'I') or (frase[j] == 'i'):
            qi += 1
        elif (frase[j] == 'O') or (frase[j] == 'o'):
            qo += 1
        elif (frase[j] == 'U') or (frase[j] == 'u'):
            qu += 1

print('A',qa)
print('E',qe)
print('I',qi)
print('O',qo)
print('U',qu)
