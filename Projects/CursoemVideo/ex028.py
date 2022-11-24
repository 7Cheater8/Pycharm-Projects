# Escreva um programa que faça o computador "pensar "em um numero inteiro esntre 0 e 5 e peça para o usuario descobrir qual foi o numero escolhido pelo computador, o programa devera escrever na tela se o usuario venceu ou perdeu
from random import randint #nao soube
computador = randint(0,5) #nao soube
print('-=-'*20)
jogador = float(input('Eu pensei em um numero, consegue adivinhar qual? . . .'))
print('-=-'*20)
if jogador <= computador:
    print('PARABENS! voce acertou')
else:
    print('EITA! pelo visto eu ganhei')
#resto soube