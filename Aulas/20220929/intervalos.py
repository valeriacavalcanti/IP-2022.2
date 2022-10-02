'''
  Exibir isso!

  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5
  1 2 3 4 5 6
  ...
  1 2 3 4 5 6 7 8 9 10
  
'''

for i in range(1,11):
    #print("i =", i)
    for j in range(1, i):
        print(j, end=" ")
    print(i)

