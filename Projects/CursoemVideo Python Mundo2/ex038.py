#Escreva um programa que leia 2 numero inteiros e compare-os mostrando na  tela uma mensagem: -O primeiro valor é maior -O segunda valor é maior -O nao existe valor maior, os 2 sao iguais
num = int(input('\033[31mPrimeiro\033[m Numero:'))
num2 = int(input('\033[34mSegundo\033[m Numero:'))
cores = { 'vermelho': '\033[31m', 'azul': '\033[34m', 'verde': '\033[32m'}
if num > num2:
    print('O {}Primeiro Numero é Maior'.format(cores['vermelho']))
elif num2 > num:
    print('O {}Segundo Numero é Menor'.format(cores['azul']))
elif num == num2:
    print('Nao existe Numero maior os dois sao {}IGUAIS'.format(cores['verde']))
#conseguir fazer sozinho