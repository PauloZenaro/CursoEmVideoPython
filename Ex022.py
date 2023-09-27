nome = str(input("Digite seu nome ")).strip()
print('Seu nome em maiusculas:', nome.upper(), '\nSeu nome em minusculas:' + nome.lower())
print('seu nome possui', len(nome) - nome.count(' '), 'letras.')
print('Seu primeiro nome tem ao todo {} letras'.format(nome.rfind(' ')))
pnome = nome.split()
print('Seu primeiro nome possui', len(pnome[0]), 'letras')
print('Seu primeiro nome é:', pnome[0])



