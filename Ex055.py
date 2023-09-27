maiorpeso = 0
menorpeso = 0

for c in range(1, 5):
    peso = float(input('Digite o peso da {}ª pessoa (Kg): '.format(c)))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso

        elif peso < menorpeso:
            menorpeso = peso

print(maiorpeso, menorpeso)
