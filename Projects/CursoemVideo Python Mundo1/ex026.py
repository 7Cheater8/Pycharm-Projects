# faça um programa que leia uma frase e mostre: quantas vezes aparece a letra 'A' em que possiçao ela aparece a primeira vez Em que posiçao ela aparece a ultima vez
frase = str(input('Digite Uma Frase:').strip())
print('A Letra A aparece {} vezes na sua Frase'.format(frase.upper().count('A')))
print('A Pirmeira Possiçao foi em {}'.format(frase.upper().find('A')))
print('A Ultima Possiçao foi em {}'.format(frase.upper().rfind('A')))
#um pouco diferente mais conseguiu