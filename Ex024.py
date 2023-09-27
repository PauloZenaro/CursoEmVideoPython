'''
cidade = input("digite o nome da cidade ")
scidade = cidade.split()
print('se 0 o nome começa com santo, se -1 não começa com santo:', scidade[0].lower().find("santo"))
'''

cidade = str(input("Em qual cidade você nasceu?")).strip()
print(cidade[:5].lower() == "santo")
