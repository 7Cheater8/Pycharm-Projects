#Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. O progrma vai perguntar o valor da casa,o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestaçao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.
cores = {'verde': '\033[31m', 'amarelo': '\033[33m', 'vermelho': '\033[32m', 'azul': '\033[34m'}
valor = float(input('Valor da Casa:'))
salario = float(input('Salario do Comprador:'))
tempo = int(input('Quantos anos de finaciamento?'))
mes = tempo * 12
total = valor / mes
pode = (salario * 30) / 100
print('\033[34m-=-\033[m'*20)
print('Para finaciar uma casa de \033[32mR$\033[m{:.2f} em {} Anos o valor é de \033[32mR$\033[m{:.2f}'.format(valor, tempo, total))
if total >= pode:
    print('Emprestimo {}NEGADO!'.format(cores['vermelho']))
else:
    print('Emprestimo {}APROVADO!'.format(cores['amarelo']))
print('\033[34m-=-\033[m'*20)
#consegui fazer sozinho :)