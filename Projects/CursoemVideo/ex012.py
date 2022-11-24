#faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preço = float(input('Valor do Produto:'))
calc = 5 * preço
perc = calc / 100
desc = perc - preço
print('Voce Tem 5% de Desconto! sendo assim o preço final é de R${:.2f}'.format(desc))

#um pouco de erros de logica no começo mais consegui