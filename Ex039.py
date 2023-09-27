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
if r < 18:
    alis = (18-r) + date.today().year
    print('Ainda {}irá{} se alistar em {} pois possui{} {}{} anos' .format(cores['verde'], cores['limpa'], alis, cores['verde'], r, cores['limpa']))
elif r == 18:
        print('{}É hora de se alistar{} pois possui{} {}{} anos' .format(cores['azul'], cores['limpa'], cores['azul'], r, cores['limpa']))
elif r > 18:
    alis =  date.today().year - (r - 18)
    print('{}Passou da hora de se alistar{} pois possui{} {}{} anos\nSeu ano de alistamento foi {}' .format(cores['vermelho'], cores['limpa'], cores['vermelho'], r, cores['limpa'], alis))
print('{} Obrigado por usar nosso programa{}' .format(cores['obg'], cores['limpa']))
