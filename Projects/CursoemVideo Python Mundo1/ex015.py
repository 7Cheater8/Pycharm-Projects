# Escreva um programa que pergunte a qunatidade de Km percoridos por um caro alugado e a quantidade de dias pelos quais foi alugado.
# Calcule o preço a pagar, sabendo que o caro custa R$60 por dia e R$0,15 Km Rodado.
day = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos foram os Km Rodados?'))
car = day * 60
otro = km * 0.15
total = car + otro
print('O Total a sr pago é de R${}'.format(total))
#consegui fazer, mais precisa de pesar mais