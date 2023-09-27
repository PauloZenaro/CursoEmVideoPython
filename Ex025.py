#nome = input("digite o nome da pessoa ")
#print("Esta na posição: ", nome.lower().find("silva"))
#print("se true existe silva no nome da pessoa, se false, não existe:", "silva" in nome)

nome = str(input("Digite seu nome: ")).strip()
print('Seu nome tem "Silva"? {}'.format('silva' in nome.lower()))
