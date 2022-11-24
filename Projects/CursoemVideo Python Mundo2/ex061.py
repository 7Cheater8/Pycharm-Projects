#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
numero = int(input('Digite o rimeiro Termo: '))
razao = int(input('Digite a Razao: '))
termo = numero
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
    print('FIM')
    #nao conseguiu