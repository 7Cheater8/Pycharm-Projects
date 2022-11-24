#faça um programa que leia um angulo quaquer e mostre na tela o valor do seno cosseno e tangente desse angulo.
from math import sin, cos, tan, radians
ângulo = float(input('Diga um Angulo Qualquer:'))
seno = sin(radians(ângulo))
print('Com o angulo de {} o SENO é {:.2f}'.format(ângulo, seno,))
coseno = cos(radians(ângulo))
print('Com o angulo {} o COSNENO é de {:.2f}'.format(ângulo, coseno))
tangente = tan(radians(ângulo))
print('Com esse angulo {} a TANGENTE é de {:.2f}'.format(ângulo, tangente))
#nao consegui muito bem