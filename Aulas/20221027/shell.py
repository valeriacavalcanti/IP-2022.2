Z:\1744888>python
Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> nome = input("Nome: ")
Nome: Valeria
>>> nome
'Valeria'
>>> type(nome)
<class 'str'>
>>> len(nome)
7
>>> nome[3]
'e'
>>> nome[3] = 'é'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> nome
'Valeria'
>>> nome += 'Maria'
>>> nome
'ValeriaMaria'
>>> len(nome)
12
>>> nome = [""]*10
>>> nomes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nomes' is not defined. Did you mean: 'nome'?
>>> nome
['', '', '', '', '', '', '', '', '', '']
>>> bits = "00001001"
>>> bits
'00001001'
>>> bin(9)
'0b1001'
>>> oct(9)
'0o11'
>>> hex(9)
'0x9'
>>> int(bits,2)
9
>>> 10 > 20
False
>>> '0' > '1'
False
>>> 'A' > 'a'
False
>>> simbolo = 'm'
>>> simbolo
'm'
>>> ord(simbolo)
109
>>> bin(ord('m'))
'0b1101101'
>>> simbolo = 'F'
>>> ord('F')
70
>>> bin(ord('F'))
'0b1000110'
>>> chr(116)
't'
>>> bin(ord('A'))
'0b1000001'
>>> bin(ord('a'))
'0b1100001'
>>> int('100000',2)
32
>>> simbolo = 'L'
>>> bin(ord(simbolo))
'0b1001100'
>>> ord('L')
76
>>> ord('l')
108
>>> bin(ord('l'))
'0b1101100'
>>> 116-32
84
>>> chr(84)
'T'
>>> 'TESTE' > 'teste'
False
>>> 'TESTE' > 'Teste'
False
>>> 'TESTE' == 'TESTE'
True
>>> '100' < '10'
KeyboardInterrupt
>>> '80' < '200'
False
>>> '100' < '10'
False
>>>