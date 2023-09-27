

'''
num = int(input("digite um número de até 4 digitos "))
n = str(num)
print('Analisando o número {}' .format(num))
print('milhar: {}' .format(n[0]))
print('Centena: {}' .format(n[1]))
print('Dezena: {}' .format(n[2]))
print('unidade: {}' .format(n[3]))
'''
'''
# Meu modelo
numero = (input("\n\ndigite um número de até 4 digitos "))
print('milhar:' + numero[0])
print('Centena:' + numero[1])
print('Dezena:' + numero[2])
print('Unidade:' + numero[3])
'''
#Melhor método - usando inteiros
num = int(input('Informe um número '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}' .format(num))
print('milhar: {}' .format(m))
print('Centena: {}' .format(c))
print('Dezena: {}' .format(d))
print('unidade: {}' .format(u))
