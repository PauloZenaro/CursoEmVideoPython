frase = str(input("digite seu texto ")).strip()
print('A letra "a" aparece ', frase.lower().count('a'), "vezes na frase.")
print('A letra "a" aparece pela primeira vez na posição ', frase.lower().find('a')+1, "na frase.")
print('A letra "a" aparece pela ultima vez na posição ', frase.lower().rfind('a')+1, "na frase.")


frase = str(input('Digite seu texto: ')).strip()
print('A letra "a" aparece {} vezes na frase.\nA letra "a" aparece pela primeira vez na posição {}\nA letra "a" aparece pela ultima vez na posição {}' .format(frase.lower().count('a'), (frase.lower().find('a')+1), frase.lower().rfind('a')+1))
