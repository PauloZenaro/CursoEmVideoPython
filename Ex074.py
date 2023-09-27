from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print (n)
print('Os quatro numeros sorteados foram: {}, {} ,{}, {}' .format(n[0], n[1], n[2], n[3]))

print(sorted(n))
print(sorted(n)[0], sorted(n)[-1])


