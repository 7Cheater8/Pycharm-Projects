# crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome ou nao
nome = str(input('Qual é o Seu nome:')).strip()
print('Seu Nome Tem Silva? {}'.format('SILVA' in nome.upper()))
#mais o menos