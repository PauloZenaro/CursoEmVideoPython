'''
n = int(input('Digite um número: '))
p = 0
for c in range(1, n+1):
    if n % c == 0:
        p = p+1
if p == 2:
    print('{} é primo' .format(n))
else:
    print('não é primo')
'''

n = int(input('Digite o número que deseja verificar: '))
p = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        p += 1
    else:
        print('\033[31m', end='')
    print('{} \033[m'.format(c), end='')

print('\nO número {} foi divido {} vezes' .format(n, p))
if p == 2:
    print('{} é um número primo' .format(n))
else:
    print('{} não é um número primo'.format(n))