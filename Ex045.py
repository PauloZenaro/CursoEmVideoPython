
from random import randint
from time import sleep

#nome = str(input('Digite seu nome: '))
#print('Olá {}\n Vamos jogar?' .format(nome))
print('Escolha sua jogada:\n1 = pedra\n2 = Tesoura\n3 = Papel')

jogadap = int(input())

print('JO')
sleep(0.2)
print('KEN')
sleep(0.2)
print('PO')
sleep(0.2)

if jogadap == 1:
    print('Você escolheu pedra')
    jogadac = randint(1, 3)

    if jogadac == 1:
        print('O computador escolheu pedra')
        print('Empate')
    elif jogadac == 2:
        print('O computador escolheu tesoura')
        print('Você ganhou')
    elif jogadac == 3:
        print('O computador escolheu papel')
        print('Você perdeu')

elif jogadap == 2:
    print('Você escolheu tesoura')
    jogadac = randint(1, 3)

    if jogadac == 1:
        print('O computador escolheu pedra')
        print('Você perdeu')
    elif jogadac == 2:
        print('O computador escolheu tesoura')
        print('Empate')
    elif jogadac == 3:
        print('O computador escolheu papel')
        print('Você ganhou')


elif jogadap == 3:
    print('Você escolheu papel')
    jogadac = randint(1, 3)
    if jogadac == 1:
        print('O computador escolheu pedra')
        print('Você Ganhou')
    elif jogadac == 2:
        print('O computador escolheu tesoura')
        print('Você perdeu')
    elif jogadac == 3:
        print('O computador escolheu papel')
        print('Empate')

else:
    print('jogada incorreta')

'''
from random import randint
from time import sleep

itens = ('Pedra', 'Tesoura', 'Papel')
computador = randint(0, 2)
print('O computador escolheu {}' .format(itens[computador])) #atenção a forma que chama a palavra.
'''
