aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = int(input('Digite a media do aluno: '))
if aluno['media'] > 6:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} = {v}')
print(aluno)
