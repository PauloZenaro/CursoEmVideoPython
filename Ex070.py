Produto = 0
preço = 0
soma = 0
maisdemil = 0
preçomaisbarato = 0
nomemaisbarato = ''


while True:
    continuar = str(input('Deseja cadastrar um produto? [S/N] ')).strip().upper()[0]
    while continuar not in 'Ss' and continuar not in 'Nn':
        continuar = str(input('Digite se sim ou não [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    if continuar in 'Ss':
        produto = str(input('Qual o nome do produto? '))
        preço = float(input('Qual o preço do produto? R$: '))
        soma += preço
        if preço > 1000:
            maisdemil += 1
        if preçomaisbarato > preço:
            preçomaisbarato = preço
            nomemaisbarato = produto
if preço != 0:
    print(f'O total é: {soma}\n{maisdemil} produtos custam mais de mil.\n O produto mais barato é {nomemaisbarato} e custa {preçomaisbarato}')
else:
    print('Obrigado')