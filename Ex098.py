from time import sleep

i = f = p = 0
def contador(i, f, p):
    print('Programa de contador de 1 a 10, 10 a 0 e o terceiro você escolhe')
    i = int(input('Digite o número inicial: '))
    f = int(input('Digite o numero final: ')) + 1
    p = int(input('Digite o passo: '))
    if p < 0:
        p *= -1
    if p == 0:
        p == 1
    if i > f:
        p *= -1
    for c in range(1, 11):
        print(c, end=' ', flush=True)
        sleep(0.2)
    print()
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.2)
    print()
    for c in range(i, f, p):
        print(c, end=' ', flush=True)
        sleep(0.2)
    print()
    print('Obrigado!')

contador(i, f, p)