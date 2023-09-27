def escreva(texto):
    numnome = len(texto) + 4
    print('~' * numnome)
    print(f'{texto:^{numnome}}')
    print('~' * numnome)

nome = str(input('Digite um texto: ')).strip()
escreva(nome)
escreva('Paulo')