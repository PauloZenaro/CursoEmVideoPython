from time import sleep
cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'limpa': '\033[m',
         'obg': '\033[4;36m'
         }

n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
media = (n1 + n2) / 2
print("Calculando.", end=''),
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
if media < 5.0:
    print('{}Reprovado{}' .format(cores['vermelho'], cores['limpa']))
elif 5.0 <= media <= 6.9:
    print('{}Recuperação{}' .format(cores['verde'], cores['limpa']))
else:
    print('{}Aprovado{}'.format(cores['azul'], cores['limpa']))
