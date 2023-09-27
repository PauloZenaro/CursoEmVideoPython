saque = 0
print('Seu dinheiro sairá em notas de 50, 20, 10, 5 e 1 real')
saque = int(input('Quanto deseja sacar? '))
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

while saque > 200:
    saque -= 50
    nota50 += 1
while saque > 60:
    saque -= 20
    nota20 += 1
while saque > 20:
    saque -= 10
    nota10 += 1
while saque > 5:
    saque -= 5
    nota5 += 1
while 0 < saque <= 5:
    saque -= 1
    nota1 += 1

print('''Seu dinheiro sera entregue em:
{} notas de 50
{} notas de 20
{} notas de 10
{} notas de 5
{} notas de 1
 '''.format(nota50, nota20, nota10, nota5, nota1))
