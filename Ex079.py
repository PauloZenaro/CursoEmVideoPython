lista = list()
cont = 'S'
while True:
    if cont == 'N':
        break
    n = int(input('Digite um número: '))

    if n in lista:
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    elif n not in lista:
        lista.append(n)
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
print(lista.sort())

