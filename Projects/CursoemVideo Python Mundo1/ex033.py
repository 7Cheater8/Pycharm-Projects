#faça um prgrama que leia 3 numeros e mostre qual é o maior e qual é o menor
a = int(input('Diga um Numero:'))
b = int(input('Diga Outro:'))
c = int(input('Diga Outro:'))
#Testando o Menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Testando o Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior Valor digitado foi {}'.format(maior))
#finish