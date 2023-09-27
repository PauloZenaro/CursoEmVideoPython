c = 0
n = int(input('Digite o número que irá iniciar a PA '))
r = int(input('Digite a razão da PA '))

while c != 10:
    print('{} ' .format(n), end='')
    n += r
    c += 1
