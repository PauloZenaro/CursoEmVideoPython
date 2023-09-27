idade = 0
maiores = 0
homens = 0
mmenores = 0

while True:
    continuar = str(input('Deseja cadastrar uma pessoa? [S/N] ')).strip().upper()[0]
    while continuar not in 'Ss' and continuar not in 'Nn':
        continuar = str(input('Digite se sim ou não [S/N] ')).strip().upper()[0]

    if continuar in 'Nn':
        break
    if continuar in 'Ss':
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
        while sexo not in 'FfMm':
            sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if idade > 18:
            maiores += 1
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff' and idade < 20:
            mmenores += 1

print(
    f'{maiores} pessoas cadastradas são maiores de 18\n{homens} pessoas cadastradas são homens\n{mmenores} são mulheres menores de 20 anos.')
