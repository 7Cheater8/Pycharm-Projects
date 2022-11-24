#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
print('\033[36m-==-\033[m'*20)
jogador = int(input('\033[35mEu pensei em um numero de 0 a 10, consegue adivinhar qual é?\033[m'))
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('\033[31m. . .hmm errou tenta denovo:\033[m'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else: #nao consegiu
        if jogador < computador:
            print('Mais . . . tente novamente')
        elif jogador > computador:
            print('Menos . . . tente novamente')
print('\033[33mVoce Acertou! BOA!\033[m')
print('\033[1;mVoce acertou com {} tentativas Parabens!\033[m'.format(palpite))
print('\033[36m-==-\033[m'*20)
#consegiu