#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
#Mais uma vez eu usei o int mais era o float
n = float(input('Uma Distancia em Metros:'))
c = n * 100
m = n * 1000
print('{} Em centimetros é {}cm e em milimetros é {}mm'.format(n, c, m))
