cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'limpa': '\033[m',
         'obg': '\033[4;36m'
         }

print('||   {}iMC{}   ||' .format(cores['obg'], cores['limpa']))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** altura)
print('{}IMC = {:.2f}{}' .format(cores['obg'], imc, cores['limpa']))

if imc < 18.5:
    print('Abaixo do peso')

elif 18.5 < imc < 25:
    print('peso ideal')

elif 25 <= imc < 30:
    print('Sobrepeso')

elif 30 <= imc < 35:
    print('Obesidade grau 1')

elif 35 <= imc < 40:
    print('Obesidade grau 2')

elif imc <= 40:
    print('Obseidade grau 3 ou Mórbida')
