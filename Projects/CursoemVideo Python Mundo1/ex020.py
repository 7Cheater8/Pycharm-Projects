#o mesmo professor qo desafio anterior quer sortear  ordem de apresentaçao de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
n1 = str(input('Aluno1:'))
n2 = str(input('Aluno2:'))
n3 = str(input('Aluno3:'))
n4 = str(input('Aluno4:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de Grupos que vai apresentar primeiro é:')
print(lista)
#conseguiu