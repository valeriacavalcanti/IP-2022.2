s = input()
criptografada = ''

for i in range(len(s)):
    # cod_atual = ord(s[i])
    # cod_prox = cod_atual + 1
    # print(s[i], cod_atual, cod_prox, chr(cod_prox))

    if ((s[i] >= 'A') and (s[i] <= 'Z')) or ((s[i] >= 'a') and (s[i] <= 'z')):
        if (s[i] == 'z'):
            proximo = 'a'
        elif (s[i] == 'Z'):
            proximo = 'A'
        else:
            proximo = chr(ord(s[i]) + 1)
        # print(proximo, end='')
        criptografada += proximo
    else:
        # print(s[i], end='')
        criptografada += s[i]
# print()

print(s)
print(criptografada)