#faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome separadamente ex Nan maria de souza primeiro: Ana ,ultimo: Souza
nome = str(input('Digte Seu Nome:')).strip()
div = nome.split()
print('O Pirmeiro nome é: {}'.format(div[0]))
print('O Ultimo nome é: {}'.format([len(nome)-1]))
#conseguiu mais nao soube o fim da ultima linha