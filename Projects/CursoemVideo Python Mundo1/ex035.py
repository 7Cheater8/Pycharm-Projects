#desenvolva um programa que leia o comprimeto de 3 retas e diga se elas podem ou nao formar um triangulo
print('\033[1;34m-☼-'*20, '\033[m')
print('              \033[1;33mAnalizando Segmentos de Retas \033[m')
print('\033[1;34m-☼-'*20, '\033[m')
cores = {'verde': '\033[32m', 'vermelho': '\033[31m'}
r1 = float(input('Digite o primeiro segmento:'))
r2 = float(input('Digite o segundo segmento:'))
r3 = float(input('Digite o terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes Segmentos {}PODEM FORMAR UM TRIANGULO!'.format(cores['verde']))
else:
    print('Estes Segmentos {}NAO PODEM FORMAR UM TRIANGULO!'.format(cores['vermelho']))
print('\033[35mFIM')
# execute para lembrar :)