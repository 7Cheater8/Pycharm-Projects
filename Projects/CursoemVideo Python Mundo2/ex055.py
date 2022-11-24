#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
for pess in range (1, 6):
    peso = float(input('Qual o {}ª peso? '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso liquido lido foi {:.2f}Kg'.format(maior))
print('O menor peso liquido lido foi {:.2f}Kg'.format(menor))
#consegiu