#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome maiusuculo, Minusculo, quantas letras ao todo (sem os espaços) e quantas letra tem o primeiro nome
nome = str(input('Qual o seu Nome Completo:')).strip()
print('Analizando seu nome . . .')
print('Seu Nome em Maiusculas é: {}'.format(nome.upper()))
print('Seu Nome em Minusculas é: {}'.format(nome.lower()))
print('Seu nome ao Todo tem {} Letras'.format(len(nome) - nome.count(' ')))
div = (nome.split())
print('E Seu Pirmeiro nome tem {} Letras'.format(len(div)))

#conseguiu (ferrugem)