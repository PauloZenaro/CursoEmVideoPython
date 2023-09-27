from random import randint
maior = 0
def maior(*num):
    print(num)
    for c in range(0, len(num)):
        if c == 0:
            maior = num[c]
        if maior < num[c]:
            maior = num[c]
    print(maior)

maior(randint(0, 100), randint(0,100), randint(0,100), randint(0,100),randint(0, 100), randint(0,100), randint(0,100), randint(0,100),randint(0, 100), randint(0,100), randint(0,100), randint(0,100))

maior(1, 5, 10)

