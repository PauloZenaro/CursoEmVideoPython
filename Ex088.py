from random import sample
from time import sleep
palpite = []
temp = []
n = 0
n = int(input('Quantas sugestões você deseja? '))
for c in range(0, n+1):
    temp = sample(range(1, 61), k=6)
    temp.sort()
    palpite.append(temp[:])
    temp.clear()
#palpite.append(sample(range(0, 60), k=6))

for c in palpite:
    print(f'{c}')
    sleep(.5)
