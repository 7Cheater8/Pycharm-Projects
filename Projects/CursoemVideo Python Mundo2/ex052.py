#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[1;mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('\033[33mE por isso ele é PRIMO\033[m')
else:
    print('\033[31mE por isso ele NAO É PRIMO\033[m')
