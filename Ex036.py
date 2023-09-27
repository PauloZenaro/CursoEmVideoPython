casa = float(input('Valor do imóvel:\033[34m '))
salario = float(input('\033[msálario mensal:\033[34m '))
vezes = int(input('\033[mPrestações:\033[33m '))

prest = casa / vezes
print('\033[mO Valor da parcela será: {}{:.2f}{}' .format('\033[34m', prest, '\033[m'))

if prest <= (salario * 0.30):
    print('\033[4;33m Parabéns! Financiamento aprovado\033[m')
elif prest >= (salario * 0.30):
    print('\033[4;31m Lamentamos! Financiamento reprovado\033[m')
