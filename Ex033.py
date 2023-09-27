n1 = (input('Digite o primeiro número: '))
n2 = (input('Digite o segundo número: '))
n3 = (input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print("{} é o maior numero".format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior número'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior número'.format(n3))
if n1 < n2 and n1 < n3:
    print("{} é o menor numero".format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor número'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor número'.format(n3))
