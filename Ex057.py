#sexo = ' '
#while sexo not in 'FMfm':
#    sexo = str(input('Digite seu sexo [F/M]: '))

sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    print('Opção \033[31minválida\033[m. Tente novamente!')
    sexo = str(input('Digite seu sexo [F/M]: '))

idade = int(input('Digite sua idade: '))
while not 0 < idade < 110:
    print('Idade \033[31minválida\033[m. Tente novamente!')
    idade = int(input('Digite sua idade: '))