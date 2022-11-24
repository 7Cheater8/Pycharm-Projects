#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:– à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('\033[1;33m LOJA DO CHE \033[m'))
preço = float(input('Qual é o Valor das compras? R$'))
print('''
Digite [1] A vista Dinheiro/Cheque
Digite [2] A vista no Cartão
Digite [3] 2x no Cartão
Digite [4] 3x ou mais No Cartão
''')
opçao = int(input('Qual a Forma de Pagamento? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
    print('Você obteve 10% de Desconto o total a ser pago é de R${:.2f}'.format(total))
elif opçao == 2:
    total = preço - (preço * 5 / 100)
    print('Você obteve 5% de Desconto o total a ser pago é de R${:.2f}'.format(total))
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Você não obteve nenhum Desconto,voçê ira pagar 2 parcelas de {:.2f} o total a ser pago é de R${:.2f}'.format(parcela, total))
elif opçao == 4:
    parcela = float(input('Quantas vezes quer parcelar? '))
    total = preço + (preço * 20 / 100)
    vezes = total / parcela
    print('Você ira pagar {:.0f} parcelas de {:.2f} o total a ser pago é de {:.2f} com 20% de juros'.format(parcela, vezes, total))
else:
    print('\033[31m [ERRO] OPÇAO INVALIDA, TENTE NOVAMENTE \033[m')