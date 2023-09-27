from datetime import date
pessoa = dict()
anoapos = 0


pessoa['Nome'] = str(input('Digite o nome: '))
pessoa['Idade'] = date.today().year - int(input('Digite o ano de nascimento: '))
pessoa['CTPS'] = int(input('Digite a CTPS: '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['Salário'] = int(input('Digite o sálario: '))
    pessoa['Ano de aposentadoria'] = pessoa['Ano de contratação'] + 35
    pessoa['Idade de aposentadoria'] = pessoa['Ano de aposentadoria'] - date.today().year + pessoa['Idade']


#print(pessoa.keys())
#print(pessoa.values())

for k, v in pessoa.items():
    print(f'{k} = {v}')
