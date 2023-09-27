'''
c = 0
s = 0
cont = 0
while c != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        c = n
    else:
        cont += 1
        s += n
print('A soma dos valores é \033[32m{}\033[m' .format(s))
print(cont)
'''
num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero: '))
print('Você digitou {} números e a soma deles é: {}' .format(cont, soma))
