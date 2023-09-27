times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians',
         'Internacional', 'Fluminense', 'Cuiába', 'Athletico-PR', 'Atlético-GO', 'São Paulo',
         'Ceará SC', 'Santos', 'Bahia', 'América-MG', 'Juventude', 'Grêmio', 'Sport Recife',
         'Chapecoense')

#print(times[0:5], '\n')


#for c in times:
#    print(c)

#for c in range(0,len(times)):
#    print(times[c])

for c in range(0, 5):
    print('\033[34m{}\033[m esta na {}{}{}ª posição' .format(times[c], '\033[34m', c+1, '\033[m'))

#print(times[-1:-5:-1])

print('\n')

for c in range(len(times) - 4, len(times)):
    print(f'\033[31m{times[c]}\033[m esta na \033[31m{c}\033[mª posição ')

print('\n')

print(f'{sorted(times)}')

pos = times.index('Chapecoense')
pos += 1
print(pos)

