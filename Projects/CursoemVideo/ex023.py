# Faça um programa que leia um niumero de - a 9999 e mostre na tela cada um dos digitos separados Ex: Digite um Numero: 1834 Unidade: 4 dezen:3 centena:8 milhar:1
num = int(input ('Digitre um Numero:'))
print('Analizando o Numero {}'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
#quase conseguiu