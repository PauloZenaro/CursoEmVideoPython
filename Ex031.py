d = int(input('Quantos quilometros tem a viagem? '))
if d <= 200:
    d = d * 0.50
else:
    d = d * 0.45
print("O valor da passagem é: R$:{:.2f}" .format(d))
