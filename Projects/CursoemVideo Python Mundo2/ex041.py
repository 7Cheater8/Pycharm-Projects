#a confederaçao nacional de nataçao precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade:
# ate 9 anos: mirim ate 14 anos:infantil ate 19 anos: junior ate20 anos: senior acima: master
from datetime import date
print('\033[35m        Veja aqui em qual categoria de nadadores você se encaixa\033[m')
print('\033[36m-==-\033[m'*20)
atual = date.today().year
ano = int(input('Qual é o se ano de nascimento? '))
idade = atual - ano
if idade <= 9:
    print('Com {} anos você é um nadador\033[31m MIRIM \033[m'.format(idade))
elif idade < 14:
    print('Com {} anos você é um nadador\033[32m INFANTIL \033[m'.format(idade))
elif idade <= 19:
    print('Com {} anos você é um nadador\033[33m JUNIOR \033[m'.format(idade))
elif idade <= 25:
    print('Com {} anos você é um nadador\033[34m SENIOR \033[m'.format(idade))
elif idade > 20:
    print('Com {} anos você é um nadador\033[35m MASTER \033[m'.format(idade))
#consegui fazer