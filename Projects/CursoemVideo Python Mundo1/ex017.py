#Faça um programa que leia o comprimetnto do cateto oposto e do cateto adjante de um triangulo retangulo e mostre o comprimento da hipotenusa.
from math import hypot
op = float(input('Cumprimeto do Cateto Oposto:'))
ad = float(input('Comprimeto do Cateto Adjacente:'))
hi = hypot(op, ad)
#hi = (op ** 2 + ad ** 2)**(1/2)
print('Com {} e {} o Comprimento da hipotenusa é: {:.2f}'.format(op, ad, hi))
#+ou-
