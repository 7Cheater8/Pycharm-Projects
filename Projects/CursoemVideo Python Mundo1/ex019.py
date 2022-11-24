#Um professor quer sortear um dos seus 4 alunos para apagar o quadro, faça um progrma que ajude a ele lendo o nome deles e escrevendo o nome do escolhido
from random import choice
n1 = str(input('Primeiro Aluno:'))
n2 = str(input('Segundo Aluno:'))
n3 = str(input('Terceiro Aluno:'))
n4 = str(input('Quarto Aluno:'))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print('O Aluno Sorteado é o {}'.format(sorteado))
#mais o menos