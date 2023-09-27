from datetime import date
maior = 0
menor = 0
for c in range (0,7):
    ano = int(input('Digite o ano de nascimento (yyyy): '))
    if(date.today().year - ano < 18):
        menor = menor + 1
    else:
        maior = maior + 1
print('O numero de pessoas maiores de idade é: {} e menores de idade: {}' .format(maior, menor))
