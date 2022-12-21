import funcoes

# PROGRAMA PRINCIPAL

nomes = []
valores = []
formas = []

# for i in range(4):
    # nomes.append(input('Informe o nome: '))
    # valores.append(float(input('Informe a compra: ')))
    # formas.append(int(input('Informe a forma de pagamento: ')))

arq = open('dados.csv', 'r')
for linha in arq.read().splitlines():
    nome, valor, forma = linha.split(';')
    valor, forma = float(valor), int(forma)
    nomes.append(nome)
    valores.append(valor)
    formas.append(forma)

# valor médio das compras
print('Valor médio:', funcoes.media(valores))

# maior valor vendido e cupons
valor = funcoes.maior(valores)
qtde = funcoes.cupons(valor)
print('Maior valor:', valor, '- Cupons:', qtde)

# total dos descontos
total = 0
for i in range(200):
    total += funcoes.desconto(valores[i], formas[i])
print('Total dos descontos:', total)

# senhas dos clientes
for i in range(200):
    print(funcoes.senha(nomes[i]))

# menor lance único e respectivo comprador
menor = funcoes.menor(valores)
if (menor >= 0):
    for i in range(200):
        if (valores[i] == menor):
            print(nomes[i])
            break
else:
    print('Nenhum lance único.')
