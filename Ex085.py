
lista = [[], []]
num = 0
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º numero: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'{lista[0]}\n{lista[1]}')


'''
numeros = list()
temppares = list()
tempimpares = list()
n = 0
sair = 'N'
while True:
    if sair == 'S':
        break
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        temppares.append(n)
    else:
        tempimpares.append(n)
    sair = input('Deseja sair? [s/n]: ').strip().upper()[0]

numeros.append(tempimpares[:])
numeros.append(temppares[:])
print(numeros)
numeros[0].sort()
print(numeros)

'''