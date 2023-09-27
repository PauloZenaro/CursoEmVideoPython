media = 0
c = 0
soma = 0
div = 1
maior = 0
menor = 0
r = str(input('Deseja executar o programa? [s/n]: ')).strip().upper()[0]
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            n = menor
    c += 1
    r = str(input('Deseja continuar ? [s/n]: ')).strip().upper()[0]
    if r in 'Nn':
        div = c
if soma != 0:
    media = soma / div
    print('A média dos números digitados é: {}' .format(media))
    print('O menor número digitado foi: {} e o maior {}' .format(menor, maior))
    print('Obrigado por usar o programa')
else:
    print('Obrigado por usar o programa')
