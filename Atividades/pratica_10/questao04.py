import tempo

# ler o tempo natação
h, m, s = input("Tempo Natação:").split()
h, m, s = int(h), int(m), int(s)
# converter h m s -> segundos! --> tempo_natacao
tempo_natacao = tempo.converter_segundos(h, m, s)

# ler o tempo ciclismo
h, m, s = input("Tempo Ciclismo:").split()
h, m, s = int(h), int(m), int(s)
# converter h m s -> segundos! --> tempo_ciclismo
tempo_ciclismo = tempo.converter_segundos(h, m, s)

# ler o tempo na corrida
h, m, s = input("Tempo Corrida:").split()
h, m, s = int(h), int(m), int(s)
# converter h m s -> segundos! --> tempo_corrida
tempo_corrida = tempo.converter_segundos(h, m, s)

tempo = tempo_natacao + tempo_ciclismo + tempo_corrida

# exibir o tempo total da prova (h, m, s)
