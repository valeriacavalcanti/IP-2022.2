controle = 7
for i in range(1, 10, 2):
    print("I={} J={}".format(i, controle))
    print("I={} J={}".format(i, controle - 1))
    print("I={} J={}".format(i, controle - 2))
    controle += 2
