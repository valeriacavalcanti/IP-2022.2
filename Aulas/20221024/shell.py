Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lista = []
lend(lista)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    lend(lista)
NameError: name 'lend' is not defined. Did you mean: 'len'?
len(lista)
0
lista.append(10)
lista
[10]
lista.append(12.8)
lista
[10, 12.8]
lista.append("IFPB")
lista
[10, 12.8, 'IFPB']
lista.append(True)
lista
[10, 12.8, 'IFPB', True]
lista.append([20,30])
lista
[10, 12.8, 'IFPB', True, [20, 30]]
lista = [[10],[20,30],[40,50,60]]
lista
[[10], [20, 30], [40, 50, 60]]
len(lista)
3
matriz = [[10,20,30],[40,50,60],[70,80,90]]
type(matriz)
<class 'list'>
len(matriz)
3
matriz[2][0]
70
matriz[2][0] = 100
mariz
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    mariz
NameError: name 'mariz' is not defined. Did you mean: 'matriz'?
matriz
[[10, 20, 30], [40, 50, 60], [100, 80, 90]]




m = [[0]*4,[0]*4,[0]*4]
m
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
m[1][0] = 12
m
[[0, 0, 0, 0], [12, 0, 0, 0], [0, 0, 0, 0]]
m = [[0]*4]*3
m
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
m[1][0] = 12
m
[[12, 0, 0, 0], [12, 0, 0, 0], [12, 0, 0, 0]]


lista = [1,2,3]
lista
[1, 2, 3]
copia = lista
copia
[1, 2, 3]
lista[0] = 10
lista
[10, 2, 3]
copia
[10, 2, 3]
copia = lista[:]
copia
[10, 2, 3]
lista
[10, 2, 3]
lista[0] = 1
lista
[1, 2, 3]
copia
[10, 2, 3]



m = []
for i in range(3):
    m.append([0]*4)

    
m
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
m[1][0] = 12
m
[[0, 0, 0, 0], [12, 0, 0, 0], [0, 0, 0, 0]]




import random
random.randint(2,6)
2
>>> random.randint(2,6)
3
>>> random.randint(2,6)
6
>>> random.randint(2,6)
5
>>> random.randint(2,6)
3
>>> random.randint(2,6)
4
>>> random.randint(2,6)
3
>>> random.randint(2,6)
5
>>> random.randint(2,6)
4
>>> random.randint(2,6)
5
>>> random.randint(2,6)
2
>>> random.randint(2,6)
2
>>> random.randint(2,6)
5
