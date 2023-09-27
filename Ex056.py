somaidade = 0
mediaidade = 0
somaidade = 0
idadehomemmaisvelho = 0
mulheresmenos20 = 0

quantidade = int(input('Quantas pessoas deseja listar: '))
for c in range(1, quantidade + 1):
    print('---------{}ª--------' .format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    somaidade += idade

    if sexo == 'M' and idade > idadehomemmaisvelho:
        nomehomemaisvelho = nome
        idadehomemmaisvelho = idade

    if sexo == 'F' and idade < 20:
        mulheresmenos20 = mulheresmenos20 + 1

mediaidade = somaidade / quantidade
print('A media das 4 idades é {}{}{}' .format('\033[034m', mediaidade, '\033[m'))

if idadehomemmaisvelho != 0:
    print('o homem mais velho é: {}{}{} e possui: {}{}{} Anos' .format('\033[034m', nomehomemaisvelho, '\033[0m',
                                                                   '\033[034m', idadehomemmaisvelho, '\033[m'))
else:
    print('Não existem homens na lista')

if mulheresmenos20 >= 2:
    print('Existem {}{}{} mulheres menores de 20 anos nesta lista' .format('\033[034m', mulheresmenos20,'\033[m'))
elif mulheresmenos20 == 1:
    print('Existe {}uma{} mulher menor de 20 anos nesta lista'.format('\033[034m', mulheresmenos20, '\033[m'))
elif mulheresmenos20 == 0:
    print('Não Existem mulheres menores de 20 anos nesta lista')