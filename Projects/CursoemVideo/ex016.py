#Crie um programa qeu leia um numero real qualquer pelo teclado e mostre na tela a sua  porçao inteira.
#Ex: Digite um numero: 6.127 O numero 6.127 tem a parte inteira 6
'''from math import trunc
num = float(input('Digite um numero real: '))
print('O numero digitado foi {} o sua porçao inteiro é {}'.format(num, trunc(num)))'''

num = float(input('Digite um Valor Real:'))
print('O Valor digitado foi {} e a sua porçao é {}'.format(num, int(num)))
