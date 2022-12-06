import copa

resultados = copa.ler_csv()

print('Edicoes:', copa.edicoes(resultados))

print('Sedes:', copa.sedes(resultados))

print('Brasil Campeao:', copa.brasil_campeao(resultados))

print('Premiacoes do Brasil:', copa.premiacoes_brasil(resultados))

print('Paises com titulos:', copa.titulos(resultados, 1))

print('Paises em segundo:', copa.titulos(resultados, 2))

print('Paises em terceiro:', copa.titulos(resultados, 3))

print('Paises em quarto:', copa.titulos(resultados, 4))

print('Mais titulos:', copa.maior_titulos(resultados))

print('Paises na final:', copa.participacao_final(resultados))
