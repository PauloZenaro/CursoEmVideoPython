v = int(input('Qual a velocidade registrada do veiculo? '))
if v<=80:
    print("Veiculo dentro do limite de velocidade")
else:
    print("Veículo acima do limite permitido\nAplicando multa\nValor R$:{:.2f}" .format((v-80)*7))


'''
v = int(input('Qual a velocidade registrada do veiculo? '))
if v >= 80:
    print("Veículo acima do limite permitido\nAplicando multa\nValor R$:{:.2f}".format((v - 80) * 7))

print('Tenha um bom dia! Dirija com segurança')
'''


