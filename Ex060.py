n = int(input('Digite o número que deseja saber o fatorial: '))
c = n
f = 1
while c > 0:
    print(' {} ' .format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    f = f * c
    c -= 1
print(f)

'''
from math import factorial
n = int(input('Digite o número que deseja saber o fatorial: '))
print ('{}' .format(factorial(n)))
'''