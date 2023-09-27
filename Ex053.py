frase = str(input('Digite a frase: ')).upper().strip()
separado = frase.split()
junto = ''.join(separado)
oposto = ''
for c in range(len(junto)-1,-1,-1):
    oposto += junto[c]
print(oposto)
if oposto == junto:
    print('\033[34m{}\033[m é um palindromo' .format(frase))
else:
    print('\033[34m{}\033[m não é um palindromo' .format(frase))