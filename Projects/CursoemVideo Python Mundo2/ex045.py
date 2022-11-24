#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
print('''
Suas opçoes
[0]\033[1;37m PEDRA \033[m
[1]\033[1m PAPEL \033[m
[2]\033[1;35m TESOURA \033[m
''')
print('-='*20)
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))
print('-='*20)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if jogador == 0:
        print('COMPUDATOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
