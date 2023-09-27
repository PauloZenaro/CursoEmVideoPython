from datetime import date
from time import sleep
cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'limpa': '\033[m',
         'obg': '\033[4;36m'
         }
nasc = int(input('Digite o ano do seu nascimento: '))
r = date.today().year - nasc
print("Calculando.", end=''),
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)

if 0 < r < 9:
    print(r)
    print('{}Mirim{}' .format(cores['azul'], cores['limpa']))
elif 9 < r <= 14:
    print(r)
    print('{}Infantil{}' .format(cores['azul'], cores['limpa']))
elif 14 < r <= 19:
    print(r)
    print('{}Junior{}'.format(cores['azul'], cores['limpa']))
elif 19 < r <= 25:
    print(r)
    print('{}Senior{}'.format(cores['azul'], cores['limpa']))
elif r > 25:
    print(r)
    print('{}Master{}'.format(cores['azul'], cores['limpa']))
else:
    print('idade inválida')
print('{} Obrigado por usar nosso programa{}' .format(cores['obg'], cores['limpa']))
