matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
#print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''
linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]

for c in range (0, 3):
    linha1[c].append(int(input('Digite um numero')))
for c in range (0, 3):
    linha2[c].append(int(input('Digite um numero')))
for c in range (0, 3):
    linha3[c].append(int(input('Digite um numero')))
print(f'{linha1}\n{linha2}\n{linha3}')
'''


