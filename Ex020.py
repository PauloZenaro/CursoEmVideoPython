from random import sample

nome1 = input("Digite o primeiro nome ")
nome2 = input("Digite o primeiro nome ")
nome3 = input("Digite o primeiro nome ")
nome4 = input("Digite o primeiro nome ")

print("{}".format(sample([nome1, nome2, nome3, nome4], k=4)))
