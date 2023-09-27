from random import randint

jogada = dict()

jogada['jogador 1'] = randint(1, 6)
jogada['jogador 2'] = randint(1, 6)
jogada['jogador 3'] = randint(1, 6)
jogada['jogador 4'] = randint(1, 6)

for c, v in jogada.items():
    print(f'O {c} tirou {v}')


for c, v in jogada.items:

    print(f'{c} tirou: {v}')
