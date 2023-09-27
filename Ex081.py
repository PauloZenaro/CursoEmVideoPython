lista = list()
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


print(f'Foram digitados: {len(lista)} numeros nesta lista')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('Existe o número 5 ná lista')

    for v, c in enumerate(lista):
        if c == 5:
            print('Na posição {}, ' .format(v))
        else:
            print('O numero 5 não está na lista')
    