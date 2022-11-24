#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos
frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
print('o inverso de {} é {}'.format(frase, inverso))
if inverso == junto: print('Temos um Palindromo')
else: print('Não é um Palindromo')
#nao consegui