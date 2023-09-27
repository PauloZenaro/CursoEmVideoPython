l = 0
c = 0
def área(l, c):
    print('                      Controle de terrenos        ')
    print('-' * 70)
    l = float(input('Digite a largura (m): '))
    c = float(input('Digite o comprimento (m): '))
    print('-' * 70)
    area = l * c
    print(f'A área de um terreno com largura: {l:.2f} metros e comprimento: {c:.2f} metros é de: {area:.2f} m²')
    print('-' * 70)

#print('Controle de terreno')
#área(float(input('Digite a largura (m): ')), float(input('Digite o comprimento (m): ')))
área(l, c)
