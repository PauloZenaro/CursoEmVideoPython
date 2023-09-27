
from random import randint
from time import sleep
tentativa = 1
n1 = int(randint(0, 10))
print('-=-' * 15)
print('Vou pensar me um número entre 0 e 10. Tente adivinhar!')
print('-=-' * 15)
print(n1)
n2 = int(input('Digite um numero de 0 a 10: '))

while n1 != n2:
    n2 = int(input('Número errado, Digite outro número de 0 a 10: '))
    tentativa += 1

#print("Pensando.", end=''),
#sleep(0.5)
#print('.', end='')
#sleep(0.5)
#print('.')
#sleep(0.5)
print('Numero igual ao da máquina, Parabéns!!!')
print('Foram necessárias {}{}{} tentativas' .format('\033[34m', tentativa, '\033[m'))

'''
# modelo que a máquina atualiza a cada erro

from random import randint
from time import sleep
n1 = int(randint(0, 3))
print('-=-' * 15)
print('Vou pensar me um número entre 0 e 3. Tente adivinhar!')
print('-=-' * 15)
n2 = int(input('Digite um numero de 0 a 3:'))
while n1 != n2:
    n1 = int(randint(0, 3))
    n2 = int(input('Número errado. Digite um numero de 0 a 3:'))

#print("Pensando.", end=''),
#sleep(0.5)
#print('.', end='')
#sleep(0.5)
#print('.')
#sleep(0.5)

print('Numero igual ao ao que pensei! Parabéns!!!')
'''