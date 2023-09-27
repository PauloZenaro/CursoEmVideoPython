preço = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('='*39)
print('           Tabela de preços')
print('='*39)
for pos in range(0, len(preço)):
    if pos % 2 == 0:
        print(f'{preço[pos]:.<30}R$:{preço[pos+1]:>6.2f}')
print('='*39)
