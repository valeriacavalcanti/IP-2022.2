s = input('Símbolo: ')

if (s >= '0') and (s <= '9'):
  print('Símbolo numérico')
elif (s >= 'A') and (s <= 'Z'):
  print('Letra maiúscula')
elif (s >= 'a') and (s <= 'z'):
  print('Letra minúscula')
else:
  print('Caractere especial')