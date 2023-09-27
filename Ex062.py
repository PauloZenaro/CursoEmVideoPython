c = 0
n = int(input('Digite o número que irá iniciar a PA '))
r = int(input('Digite a razão da PA '))
c1 = 0
c2 = 0
while c < 10:
    print('{} ' .format(n), end='')
    n += r
    c += 1

c1 = int(input('\nDeseja exibir mais quantos números?'))
c2 = c
c = 0
while c < c1:
    print('{} ' .format(n), end='')
    n += r
    c += 1
    c2 += 1
    if c == c1:
        c1 = c1 + int(input('Deseja exibir mais numeros? digite quantos números deseja exibir, digite 0 para encerrar: '))
        if c1 == c1 + 0:
            c = c1
print('\n', c2)
