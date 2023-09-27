dia = int(input("Quantos dias o carro ficou alugado? "))
km = int(input("Quantos KM foram rodados? "))
valor = ((km * 0.15) + (dia * 60))
print("O valor do aluguel é R$:{:.2f}" .format(valor))