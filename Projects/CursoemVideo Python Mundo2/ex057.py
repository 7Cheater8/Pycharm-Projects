#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[31m[ERRO] valor invalido, por favor tente novamente:\033[m')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

