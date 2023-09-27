n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n = (n1, n2, n3, n4)
parcount = 0

print('O numero 9 apareceu: {} vezes'.format(n.count(9)))

if n.count(3) > 0:
    print('O numero 3 apareceu pela primeira vez na {}ª posição' .format(n.index(3)+1))
else:
    print('O numero 3 não apareceu nenhuma vez')


print('os numeros pares digitados foram: ', end='')

for c in sorted(n):
    if c % 2 == 0:
        print('{} ' .format(c), end='')

    elif c % 2 != 0 and parcount != 4:
        parcount += 1

    if parcount == 4:
        print('Não foram digitados números pares')
