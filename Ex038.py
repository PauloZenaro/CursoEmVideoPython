cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'limpa': '\033[m',
         'obg': '\033[4;36m'
         }

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print("O primeiro número é {}maior{} que o segundo" .format(cores['azul'], cores['limpa' ]))
elif n1 < n2:
    print("O primeiro número é {}menor{} que o segundo".format(cores['vermelho'], cores['limpa']))
elif n1 == n2:
    print("O primeiro número é {}igual{} que o segundo".format(cores['verde'], cores['limpa']))
print('{}Obrigado por Usar nosso programa!!!{}' .format(cores['obg'], cores['limpa']))
