cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'limpa': '\033[m',
         'obg': '\033[4;36m'
         }

l1 = float(input('Digite o primeiro lado do triangulo '))
l2 = float(input('Digite o segundo lado do triangulo '))
l3 = float(input('Digite o terceiro lado do triangulo '))
if l1 < l2 + l3 and l2 < l1 + l2 and l3 < l1 + l2 or l1 == l2 == l3:

    print('É possível formar um triangulo')

    if l1 == l2 == l3:
        print('Triangulo {}Equilátero{}'.format(cores['azul'], cores['limpa']))

    elif l1 > l2 == l3 or l2 > l1 == l3 or l3 > l1 == l2:
        print('Triangulo {}Isoceles{}' .format(cores['verde'], cores['limpa']))

    elif l1 != l2 != l3 != l1:
        print('Triangulo {}Escaleno{}' .format(cores['vermelho'], cores['limpa']))


else:
    print('não é possível formar um triangulo')
