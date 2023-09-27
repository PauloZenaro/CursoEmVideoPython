'''
ano = int(input('Digite um ano YYYY: '))
if ano % 4 == 0:
    print('Ano Bissexto')
else:
    print('Ano não Bissexto')
'''
from datetime import date

ano = int(input('Digite um ano YYYY, tecle 0 para digitar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print('Ano de {} é Bissexto' .format(ano))
else:
    print('Ano de {} não é Bissexto' .format(ano))
