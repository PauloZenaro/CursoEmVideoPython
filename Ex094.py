lista = list()
c = 0
sair = 'N'
pessoas = dict()
media = 0

while True:
    if sair == 'S':
        break
    pessoas['nome'] = str(input('Digite o nome: ')).strip()
    pessoas['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()
    pessoas['idade'] = int(input('Digite a idade: '))
    media += pessoas['idade']
    c += 1
    lista.append(pessoas.copy())
    pessoas.clear()
    sair = str(input('Deseja sair?[S/N] ')).strip().upper()
media = media / c
print(lista)
print(f'Foram cadastradas {c} pessoas.')
print('As mulheres cadastradas foram: ', end='')


for cont in range(0, len(lista)):
    if lista[cont]['sexo'] == 'F':
        print(f'{lista[cont]["nome"]},')

print(f'A média de todas as idades é: {media}')
print('Estas pessoas tem a idade acima da media: ', end='')

for c in range(0, len(lista)):
    if lista[c]['idade'] > media:
        print(f'{lista[c]["nome"]} ')
