q_alcool = q_gasolina = q_diesel = 0

codigo = int(input())

while (codigo != 4):
    if (codigo == 1):
        q_alcool += 1
    elif (codigo == 2):
        q_gasolina += 1
    elif (codigo == 3):
        q_diesel +=1
        
    codigo = int(input())

print("MUITO OBRIGADO")
print("Alcool:", q_alcool)
print("Gasolina:", q_gasolina)
print("Diesel:", q_diesel)
