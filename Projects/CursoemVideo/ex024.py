#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com a palavra 'santo'
cid = str(input('Qual é a sua cidade:')).strip()
print(cid[:5].upper() == 'SANTO')

#mais o menos