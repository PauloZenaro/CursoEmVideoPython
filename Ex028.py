'''
from random import uniform
n1 = int(uniform(0, 5))
print(n1)
n2 = int(input('Digite um numero de 0 a 5:' ))
if n1 == n2:
    print('Numero igual ao da máquina, Parabens!!!')
else:
    print('Numero errado, o número era {} tente novamente' .format(n1))
print('FIM')
'''

from random import randint
from time import sleep
n1 = int(randint(0, 5))
print('-=-' * 15)
print('Vou pensar me um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 15)
print(n1)
n2 = int(input('Digite um numero de 0 a 5:' ))
print("Pensando.", end=''),
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
if n1 == n2:
    print('Numero igual ao da máquina, Parabéns!!!')
else:
    print('Numero errado, o número que pensei era {}, tente novamente' .format(n1))
print('FIM')
