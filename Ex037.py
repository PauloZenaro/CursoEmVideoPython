'''
]valor = int(input('Digite um número:\033[34m '))
print('{} O valor digitado foi:{}{}{}' .format('\033[m', '\033[34m', valor, '\033[m'))
print('Escolha o tipo de base que deseja converter:\n{}1{} para binário\n{}2{} para octal\n{}3{} para hexadecimal' .format('\033[35m', '\033[m', '\033[35m', '\033[m', '\033[35m', '\033[m'))
c = (int(input()))
if c == 1:
    valor = bin(valor)
    print('O valor será: {}' .format(valor))
elif c == 2:
    valor = format(valor, "o")
    print('O valor será: {}' .format(valor))
elif c == 3:
    valor = format(valor, 'x')
    print('O valor será: {}' .format(valor))
else:
    print('Escolha não existe')
print('\033[35mObrigado por usar nosso programa.\033[m')
'''

valor = int(input('Digite um número:\033[34m '))
print('{} O valor digitado foi:{}{}{}' .format('\033[m', '\033[34m', valor, '\033[m'))
print('Escolha o tipo de base que deseja converter:\n{}1{} para binário\n{}2{} para octal\n{}3{} para hexadecimal' .format('\033[35m', '\033[m', '\033[35m', '\033[m', '\033[35m', '\033[m'))
c = (int(input()))
if c == 1:
    print('O valor será: {}' .format(bin(valor)[2:]))
elif c == 2:
        print('O valor será: {}' .format(oct(valor)[2:]))
elif c == 3:
       print('O valor será: {}' .format(hex(valor)[2:]))
else:
    print('Escolha não existe')
print('\033[35mObrigado por usar nosso programa.\033[m')