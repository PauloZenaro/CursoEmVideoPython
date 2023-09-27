
d = 0
soma = 0
m = 0
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
while d != 5:
    print('''O que deseja fazer com os números digitados?
    [1] - Somar os números
    [2] - Multiplicar os números
    [3] - Saber qual é maior entre os 2
    [4] - Digitar novos números
    [5] - sair do programa''')
    d = int(input('Qual sua escolha: '))
    if d == 1:
        soma = a + b
        print('A soma é: {}{}{}' .format('\033[34m', soma, '\033[m)'))

    elif d == 2:
        m = a * b
        print('A multiplicação é: {}{}{}' .format('\033[34m', m, '\033[m)'))

    elif d == 3:
        if a > b:
            print('{} > {}'.format(a , b))
        elif a < b:
            print('{} > {}' .format(b, a))
        else:
            print('{} = {}' .format(a, b))
    elif d == 4:
        a = int(input('Digite o primeiro número: '))
        b = int(input('Digite o segundo número: '))
        d = 0
    elif d == 5:
       d = 5
    else:
        d = 0
