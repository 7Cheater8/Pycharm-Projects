#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao: 1 para binario 2 para octal 3 para hexadecimal
num = int(input('Escolha um numero:'))
print('''Escolha uma das Bases para converçao:
         [1] Para \033[31mBINARIO\033[m
         [2] Para \033[34mOCTAL\033[m
         [3] Para \033[32mHEXADECIMAL\033[m''')
base = int(input('Qual a base numerica que voce quer?'))
if base == 1:
    print('{} em \033[31mBINARIO\033[m é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} em \033[34mOCTAL\033[m é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} em \033[33mHEXADECIMAL\033[m é {}'.format(num, hex(num)[2:]))
else:
    print('\033[31m[ERRO] Opção Invalida Tente Novamente!\033[m')
