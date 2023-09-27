tupla = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte']
n = 0
n = int(input('Digite um número entre 0 e 20: '))
while 0 > n or n > 20:
    n = int(input('Digite um número entre 0 e 20: '))
print('Você digitou: {}'.format(tupla[n]))
