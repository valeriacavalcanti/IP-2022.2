frase = input("Frase: ")
st = ''

for i in range(len(frase)):
  if (frase[i] >= 'a') and (frase[i] <= 'z'):
    st += chr(ord(frase[i]) - 32)
  else:
    st += frase[i]

print(frase)
print(st)