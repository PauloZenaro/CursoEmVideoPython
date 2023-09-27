l1 = float(input('Digite o primeiro lado do triangulo '))
l2 = float(input('Digite o segundo lado do triangulo '))
l3 = float(input('Digite o terceiro lado do triangulo '))
if l1 < l2 + l3 and l2 < l1 + l2 and l3 < l1 + l2 or l1 == l2 == l3:
    print('É possível formar um triangulo')
else:
    print('não é possível formar um triangulo')
