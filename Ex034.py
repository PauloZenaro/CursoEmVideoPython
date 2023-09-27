sa = float(input("Digite o Salário do fúncionaro R$: "))
sm = float
if sa > 1250.00:
    sm = sa + (sa * 0.10)
    print("o sálario de R$:{} com aumento irá ficar: R$:{}" .format(sa, sm))
else:
    sm = sa + (sa * .15)
    print("o sálario de {} com aumento irá ficar {}" .format(sa, sm))
