soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}º numero: ' .format(c)))
    if n % 2 == 0:
        soma = soma + n
    else:
        n = 0
print('A soma dos numeros pares digitados é: {}'.format(soma))
