v_inter = 0
v_gremio = 0
empates = 0

while (True):
    inter, gremio = input().split()
    inter, gremio = int(inter), int(gremio)
    if (inter > gremio):
        v_inter += 1
    elif (inter < gremio):
        v_gremio += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    novo = input()
    if (novo == '2'):
        break

total = v_inter + v_gremio + empates
print(total, 'grenais')
print('Inter:', v_inter, sep='')
print('Gremio:{}'.format(v_gremio))
print('Empates:{}'.format(empates))

if (v_inter > v_gremio):
    print('Inter venceu mais')
elif (v_inter < v_gremio):
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
