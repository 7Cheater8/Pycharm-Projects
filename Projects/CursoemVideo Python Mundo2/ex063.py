#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo
print('-=-'*15)
print('\033[33m     Sequencia Fibonacci \033[m')
print('-=-'*15)
numero = int(input('Quantos Termos você quer mostrar? '))
print('\033[32m►-◄\033[m'*15)
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
c = 3
while c <= numero:
    t3 = t1 + t2
    print('→ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('→\033[36m FIM\033[m')
print('\033[32m►-◄' * 15)
