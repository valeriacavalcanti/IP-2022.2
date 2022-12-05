# Converter de h,m,s -> segundoS
def converter_para_segundos(hora, minuto, segundo):
    tempo = hora * 3600
    tempo += minuto * 60
    tempo += segundo
    return tempo

# Converter de segundoS -> [h, m, s]
def converter_para_hms(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return [h,m,s]
