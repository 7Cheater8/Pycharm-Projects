#Escreva um programa que escreva o salario de um funcionario e caucule o valor do seu aumento para salarios superiores a 1250R$ caucule um aumento de 10% para os inferiores ou iguais o aumento é de 15%
salario = float(input('Qual é o Valor do Salario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario = (salario * 10 / 100)
print('Quem ganhava {:.2f} agora ganha {:.2f}'.format(salario, novo))
#pulei