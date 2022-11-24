#Crie um algoritiomo que leia um numero e mostre o seu dobro triplo e raiz quadrada
#esqueci de colocar a raiz, e tambem fiz um pouco diferente
n = int(input('Digite um Numero:'))
d = n * 2 #d = n + n
t = n * 3 #t = n + n + n
r = n ** (1/2)
print('O Dobro de {} é {} e o Triplo é {}'.format(n, d, t))
print('A raiz Quadrada de {} é {}'.format(n, r))
#pow tambem caucula raiz quadrada

