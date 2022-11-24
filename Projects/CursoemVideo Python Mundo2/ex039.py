#faça um programa que leia o ano de nascimento de um jovem e infrome, de acordo com a sua idade se ele ainda vai se alistar ao serviço militar se é hora de se alistar  se ja passou do tempo do alistamento se programa tambem devera mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
nas = int(input('Em qual ano voce nasceu?'))
idade = atual - nas
print('Quem nasceu em {} Hoje tem {}'.format(nas, idade))
if idade == 18:
    print('Esta na Hora de se Alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para se Alistar'.format(saldo))
    ano = atual + saldo
    print('Voce se alista em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
    ano = saldo - atual
    print('Voce deveria ter se alistado em {}'.format(ano))

#nao consegui muito bem