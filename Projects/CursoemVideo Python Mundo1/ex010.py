#Crie um programa que leia quanto a pessao tem na carteira e mostre quantos Dolares ela pode comprar
real = float(input('Quanto voce tem na sua carteira? R$'))
dolar = real / 5.60
print('Com R${:.2f} Voce pode Comprar U${:.2f}'.format(real, dolar))
#nao consegui fazer