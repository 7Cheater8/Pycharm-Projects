#Faça um algoritimo que leia o salario de um Funcionario e mostre seu novo salario, com 15% de aumento
salario = float(input('Qual o Seu Salario Atual? R$'))
aumen = salario + (salario * 15 / 100)
print('Voce Recebeu um Aumento de 15% no Seu Salario, Agora seu salario é de: R${}'.format(aumen))

#consegui sem problemas