lista = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))

print(lista)
for c, v in enumerate(lista):
    print(c, v)
    if c == 0:
        maior = v
        menor = v
    if v >= maior:
        maior = v
    if v <= menor:
        menor = v

print(f'{lista} \n o maior numero foi: {maior} e o menor: {menor}')

for v, c in enumerate(lista):
    if c == maior:
        print(v, end=' ')
print()
for v, c in enumerate(lista):
    if c == menor:
        print(v, end=' ')
print()

#lista.sort()
#print(lista[0])
#print(lista[-1])
