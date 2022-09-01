nota1 = int(input("Primeira nota: "))
nota2 = int(input("Segunda nota: "))
nota3 = int(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Sua média é: {:.1f}".format(media))

if (media >= 70):
    print("Eita!")
    print("Aprovado!")
    print("Que bom!")
elif (media >= 40):
    print("Ainda tem chance")
    print("Final")
    print("Cuide!")
else:
    print("Vixe!")
    print("REprovado!!")
    print("Que ruim!")
