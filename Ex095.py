lista = list()
jogador = {'jogador': 'Paulo', 'Gols': [5, 4], 'total': 9}
lista.append(jogador.copy())
jogador.clear()
jogador = {'jogador': 'carlos', 'Gols': [5, 4, 2, 4, 5], 'total': 29}
lista.append(jogador.copy())
jogador.clear()
jogador = {'jogador': 'Paulo', 'Gols': [5, 4, 5, 3], 'total': 9}
lista.append(jogador.copy())
cont = 0
'''
jogador = dict()
lista = list()
temp = list()
partidas = 0
total = 0
sair = 'N'
cont = 0

while True:
    if sair == 'S':
        break
    jogador['jogador'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))

    for c in range(0, partidas):
        temp.append(int(input(f'Quantos gols ele fez na parta {c+1}: ')))
    for c in range (0, len(temp)):
        total += temp[c]
    jogador['Gols'] = temp.copy()
    jogador['total'] = total
    lista.append(jogador.copy())
    jogador.clear()
    sair = str(input('Deseja sair? [S/N] ')).strip().upper()
'''
print(lista)
print()

print('Cod        nome          gols        total')
for c in range(0, len(lista)):
    print(f' {c}         {lista[c]["jogador"]}         {[lista[c]["Gols"]]}      {lista[c]["total"]}')

while cont != 999:
    cont = int(input('Qual jogador deseja visualizar? '))
    print(f'Levantamento do jogador {lista[cont]["jogador"]}')
    for c in range(0, len(lista[cont]['Gols'])):
       #print(f'No jogo {c} fez: {lista[cont]["Gols"]}')
        print(f'No jogo {c} fez: ', end='')
        for v in lista[cont]["Gols"]:
            print(v, end='')
        print()

'''
#for k, v in jogador.items():
#   print(f'{k} é {v}')

print(f'O jogador {jogador["jogador"]} jogou {partidas} partidas no total')
for c in range(0, len(jogador['Gols'])):
    print(f'{jogador["Gols"][c]} na partida {c+1} ')
print(f'Um total de {jogador["total"]} gols')
'''