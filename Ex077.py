palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso')
vogais = ('a', 'e', 'i', 'o', 'u')


for p in palavras:
    print(f'\n{p}: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f' {letra}', end='')
