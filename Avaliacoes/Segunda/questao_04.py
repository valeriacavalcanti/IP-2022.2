texto = input('Texto: ')
nova = ''
title = ''

for i in range(len(texto)):
    if (texto[i] >= 'A') and (texto[i] <= 'Z'):
        nova += chr(ord(texto[i]) + 32)
    else:
        nova += texto[i]

# primeiro símbolo da string
if (nova[0] >= 'a') and (nova[0] <= 'z'):
    title += chr(ord(nova[0]) - 32)
else:
    title += nova[0]

# demais símboloS da string
for i in range(1, len(nova)):
    if (nova[i-1] == ' ') and (nova[i] >= 'a') and (nova[i] <= 'z'):
        title += chr(ord(nova[i]) - 32)
    else:
        title += nova[i]

print(texto)
print(nova)
print(title)