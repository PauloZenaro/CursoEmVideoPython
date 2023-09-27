#pessoas = [['Paulo', 81], ['Ana', 50], ['Rose', 60]]
pessoas = list()
dados = list()
maiorpeso = 0
menorpeso = 0
mediapeso = 0
cadastrar = 'S'
cont = 0
while True:
    while cadastrar != 'S' and cadastrar != 'N':
        cadastrar = str(input('Digite [S/N]: ')).strip().upper()[0]
    if cadastrar == 'N':
        break
    if cadastrar == 'S':
        dados.append(str(input('Digite o nome: ')))
        dados.append(int(input('Digite o peso: ')))
        if len(pessoas) == 0:
            maiorpeso = menorpeso = dados[1]
        else:
            if dados[1] > maiorpeso:
                maiorpeso = dados[1]
            if dados[1] < menorpeso:
                menorpeso = dados[1]
        pessoas.append(dados[:])
        dados.clear()
        cont += 1
        print(pessoas)
        cadastrar = str(input('Deseja cadastrar outra pessoa [S/N]: ')).strip().upper()[0]



print(f'Foram cadastradas {cont} pessoas')

for p in pessoas:
    if p[1] == maiorpeso:
        print(f'as pessoas com maior peso são: {p[0]}')
print(f'O maior peso foi {maiorpeso} kg')

for p in pessoas:
    if p[1] == menorpeso:
        print(f'as pessoas com maior peso são: {p[0]}')
print(f'O menor peso foi {menorpeso} kg\n')

#for p in pessoas:
#    print(p[1])





'''
for p in pessoas:
    if pessoas[1][1] > maiorpeso:
        maiorpeso = pessoas[p][1]
    if pessoas[1][1] < menorpeso:
        menorpeso = pessoas[p][1]
'''

