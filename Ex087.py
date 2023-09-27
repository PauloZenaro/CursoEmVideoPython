maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if l ==1 and matriz[l][c] > maior:
            maior = matriz[l][c]
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
#print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(soma)
print(maior)
