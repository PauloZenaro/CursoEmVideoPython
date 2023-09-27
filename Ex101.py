def voto(idade):
    if idade >= 18:
        return print('Voto obrigaório')
    if 16 <= idade > 18:
        return print('Voto opcional')
    if idade < 16:
        return print('Voto negado')


from datetime import date

ano = int(input('Digite o ano do seu nascimento:[yyyy]'))
ano = date.today().year - ano
voto(ano)
