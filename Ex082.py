lista = list()
pares = list()
impares = list()

cont = 'S'
while True:
    if cont == 'N':
        break
    elif cont != 'N' and cont != 'S':
        cont = str(input('Digite [S/N]: ')).strip().upper()
    else:
        n = int(input('Digite um número: '))
        lista.append(n)
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
for v, c in enumerate(lista):
    if c % 2 == 0:
        pares.append(lista[v])
    else:
        impares.append(lista[v])
lista.sort()
pares.sort()
impares.sort()
print(f'A lista de digitada é: {lista}', end='')
print()
print(f'A lista de numeros pares é: {pares}', end='')
print()
print(f'A lista de numeros impares é: {impares}', end='')

