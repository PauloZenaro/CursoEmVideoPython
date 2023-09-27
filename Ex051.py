n = int(input('Digite o número de inicio da progressão aritmética '))
r = int(input('Digite agora, a razão da progressão '))

for c in range(n, n+r*10, r):
    print(c)
