jogador = dict()
temp = list()
partidas = 0
total = 0
jogador['jogador'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))

for c in range(0, partidas):
    temp.append(int(input(f'Quantos gols ele fez na parta {c+1}: ')))
for c in range (0, len(temp)):
    total += temp[c]
jogador['Gols'] = temp.copy()
jogador['total'] = total

#for k, v in jogador.items():
#   print(f'{k} é {v}')

print(f'O jogador {jogador["jogador"]} jogou {partidas} partidas no total')
for c in range(0, len(jogador['Gols'])):
    print(f'{jogador["Gols"][c]} na partida {c+1} ')
print(f'Um total de {jogador["total"]} gols')
