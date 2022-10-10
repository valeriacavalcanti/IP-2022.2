Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = 2
type(num)
<class 'int'>
num
2
numeros = []
type(numeros)
<class 'list'>
len(numeros)
0
numeros = [10]
type(numeros)
<class 'list'>
len(numeros)
1
numeros
[10]
numeros = 20
numeros
20
type(numeros)
<class 'int'>
numeros = [10]
numeros
[10]
numeros[0] = 20
type(numeros)
<class 'list'>
numeros
[20]
print(numeros)
[20]
print(numeros[0])
20
print(numeros[1])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(numeros[1])
IndexError: list index out of range
numeros = [10,20,30,40,50]
type(numeros)
<class 'list'>
len(numeros)
5
numeros
[10, 20, 30, 40, 50]
print(numeros)
[10, 20, 30, 40, 50]
print(numeros[0])
10
print(numeros[1])
20
print(numeros[2])
30
print(numeros[3])
40
print(numeros[4])
50
for i in range(5):
    print(numeros[i])

    
10
20
30
40
50
numeros = [10,20,30,40,50,60]
numeros
[10, 20, 30, 40, 50, 60]



for i in range(5, -1, -1):
    print(numeros[i])

    
60
50
40
30
20
10
>>> print(numeros[4])
50
>>> 
>>> 
>>> for i in range(6):
...     numeros[i] = int(input("Número: "))
... 
...     
Número: 100
Número: 200
Número: 300
Número: 400
Número: 500
Número: 600
>>> numeros
[100, 200, 300, 400, 500, 600]
