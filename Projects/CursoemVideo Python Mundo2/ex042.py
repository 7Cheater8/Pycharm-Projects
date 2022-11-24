#refaça o desafio 035 dos triangulos, acresentando o recurso  de mostras que itipo de  triangulo sera formado: equilatero: todos lados sao iguais - isoceles: 2 lados iguasl e escaleno todos os lados diferentes
print('\033[34m-☼-\033[m'*20)
print('\033[1;33m             Analisando Segmentos de Retas \033[m')
print('\033[34m-☼-\033[m'*20)
cores = {'verde': '\033[32m', ' vermelho': '\033[33m'}
r1 = float(input('Digite o primeiro segmento:'))
r2 = float(input('Digite o segundo segmento:'))
r3 = float(input('Digite o terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes segmentos {}PODEM FORMAR UM TRIANGULO!'.format(cores['verde']))
    if r1 == r2 == r3:
        print('\033[1;30mTRIANGULO EQUILATERO\033[m')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('\033[1;35mTRIANGULO ISOCELES!\033[m')
    elif r1 != r2 != r3:
        print('\033[1;36mTRIANGULO ESCALENO!\033[m')
else:
    print('Estes segmentos \033[31mNAO PODEM FIORMAR UM TRIANGULO!\033[m')
print('\033[34m FIM \033[m')
#me enrolei mais no fim entendi