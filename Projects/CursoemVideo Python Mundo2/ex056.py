#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('-=-=-=-=-= Dados da {}ª pessoa -=-=-=-=-='.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A media de Idade do Grupo é de {}'.format(mediaidade))
print('O homen mais velho se chama {} e tem {} anos'.format(nomevelho, maioridade))
print('Ao todo sao {} mulher com menos de 20 anos'.format(totmulher))
#consegiu mais o menos