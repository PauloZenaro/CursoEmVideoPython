cont = 0
while True:
    n = int(input('Digite o número que deseja ver a tabuada: '))
    print('-'*20)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont} = \033[34m{n * cont}\033[m')
        cont += 1
    print('-'*20)
    cont = 0
