lista = list()
aluno = list()
temp = list()

cont = 0
sair = 'N'

while True:
    if sair in 'Ss':
        break
    aluno.append(str(input(('Digite o nome do aluno: '))))
    temp.append(int(input('Digite a primeira nota: ')))
    temp.append(int(input('Digite a segunda nota: ')))
    aluno.append(temp[:])
    lista.append(aluno[:])
    temp.clear()
    aluno.clear()
    sair = str(input('Deseja sair? [S/N]')).strip().upper()

print('=-=' * 20)
print(f'nº           Nome              Notas                 Media')
for c in range(0, len(lista)):
    print(f'{c}      {lista[c][0]:^16}       {lista[c][1][0]},{lista[c][1][1]}               {(lista[c][1][0]+lista[c][1][1])/2:>5}')

while c != 999:
    c = (int(input('Qual aluno deseja verificar? (digitar 999 fecha o programa): ')))
    if c < len(lista):
        c = 0
    print(f'O aluno {lista[c][0]} tirou {lista[c][1][0]} e {lista[c][1][1]} e sua média foi: {(lista[c][1][0]+lista[c][1][1])/2:>5}')