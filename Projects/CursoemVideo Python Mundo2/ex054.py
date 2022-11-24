#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nas = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = ano - nas
    if idade >= 21: totmaior += 1
    else: totmenor += 1
print('\033[36mAo todo tivemos {} pessoas maiores de idade\033[m'.format(totmaior))
print('\033[31mAo todo tivemos {} pessoas menores de idade\033[m'.format(totmenor))

#print('\033[36m Com {} anos esta pessoa ja atingiu a maior idade\033[m'.format(idade))
#print('\033[31mEsta pessoa ainda nao atingiu a maior idade\033[m')
#conseguiu