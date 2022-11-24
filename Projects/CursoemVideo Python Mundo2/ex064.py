#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numero = count = soma = 0
numero = int(input('Digite um numero [Digite 999 para parar]: '))
while numero != 999:
    soma += numero
    count += 1
    numero = int(input('Digite um numero [Digite 999 para parar]: '))
print('Você Digitou {} Valores e a Soma desse Valores Foi {}'.format(count, soma))
#nao conseguiu muito bem