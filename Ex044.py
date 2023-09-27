cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'limpa': '\033[m',
         'obg': '\033[4;36m'
         }

valor = float(input('Qual o valor do produto R$: '))
print('escolha a condição de pagamento:')
print('1 = A vista no dinheiro\n2 = Crédito a vista\n3 = Crédito em 2 vezes\n4 = Crédito em 3 vezes ou mais ')
cond = int(input())

if cond == 1:
    valor = valor * 0.90
    print("O valor com 10% de desconto ficará:{}{}{}" .format(cores['azul'], valor, cores['limpa']))

elif cond == 2:
    valor = valor * 0.95
    print("O valor com 5% de desconto ficará:{}{}{}" .format(cores['azul'], valor, cores['limpa']))

elif cond == 3:
    print("O valor é:{}{}{}".format(cores['azul'], valor, cores['limpa']))

elif cond == 4:
    par = int(input('Quantas vezes deseja fazer?'))
    valor = valor * 1.20
    par1 = valor / par
    print('O valor do produto com acréscimo de 20% ficará {}{}{} e cada parcela custará: {}{}{}' .format(cores['azul'], valor, cores['limpa'], cores['vermelho'], par1, cores['limpa']))
else:
    print('Valor incorreto, reiniciar o programa')
