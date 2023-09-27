from random import randint
from time import sleep
n1 = 0
n2 = 0
v = 0
soma = 0
while True:
    escolha = str(input('Escolha entre par ou impar [P/I]: ')).strip().upper()[0]
    n1 = int(input('escolha um número: '))
    n2 = randint(1, 100)
    print(f'Computador escolheu \033[31m{n2}\033[m')

    print('Contando...')
    sleep(1)
    soma = n1 + n2
    if escolha in 'Pp':
        if soma % 2 != 0:
            print(f'{soma} é impar.')
            break
        else:
            print(f'{soma} é par. Você ganhou!!!')
            v += 1
    if escolha in 'Ii':
        if soma % 2 == 0:
            print(f'{soma} é par.')
            break
        else:
            print(f'{soma} é impar. Você ganhou!!!')
            v += 1
print(f'Você perdeu.\nvocê venceu {v} vezes consecutivas\ntente novamente')
