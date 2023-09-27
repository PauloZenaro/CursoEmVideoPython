from random import randint
from time import sleep


def sorteio(lista):
    for c in range(0, 10):
        lista.append(randint(0, 100))
    print(lista)
def somapar(lista):
    soma = 0
    print('São pares os números: ', end='')
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
            print(lista[c], end=' ')
    print()
    print(f'a soma dos pares é: {soma}')

def somaimpar(lista):
    somadeimpar = 0
    print('São impares os números: ', end='')
    for c in range(0, len(lista)):
        if lista[c] % 2 != 0:
            somadeimpar += lista[c]
            print(f'{lista[c]}', end=" ")
    print()
    print(f'A soma dos impares é: {somadeimpar}')


numeros = list()


sorteio(numeros)
somapar(numeros)
somaimpar(numeros)