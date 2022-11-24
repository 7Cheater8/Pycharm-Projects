#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
numero = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
decimo = numero + (10 - 1) * razao
for c in range(numero, decimo, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')
#nao conseguiu muito bem