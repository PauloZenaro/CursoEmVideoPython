
lista = list()
lista = str(input('Digite a formula: ')).strip().lower()
lista.split()

if '(' in lista or ')' in lista:
    a = lista.count('(')
    b = lista.count(')')
if a == b:
    print('Formula válida')

else:
    print('Formula Invalida')