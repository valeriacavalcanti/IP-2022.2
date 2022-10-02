q_coelho = q_rato = q_sapo = 0
total = 0

experimentos = int(input())
for i in range(experimentos):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)

    if (tipo == 'C'):
        q_coelho += quantidade
    elif (tipo == 'R'):
        q_rato += quantidade
    else:
        q_sapo += quantidade
    

total = q_coelho + q_rato + q_sapo

print("Total:",total,"cobaias")
print("Total de coelhos:", q_coelho)
print("Total de ratos:", q_rato)
print("Total de sapos:", q_sapo)
print("Percentual de coelhos: {:.2f} %".format(q_coelho/total*100))
print("Percentual de ratos: {:.2f} %".format(q_rato/total*100))
print("Percentual de sapos: {:.2f} %".format(q_sapo/total*100))
