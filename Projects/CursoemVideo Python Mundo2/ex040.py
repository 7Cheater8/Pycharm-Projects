#crie um programa que leia 2 notas de um aluno e caucule a sua media, mostrnado no fianl de aocrdo com a media: media abaixo de 5.0:reprovado -media entre 5.0. e 6.9 recuperaçao - media 7.0 ou superior aprovado
print('\033[35m         Veja aqui se Você esta dentro da media\033[m')
print('\033[36m-=-\033[m'*20)
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
print('\033[36m-=-\033[m'*20)
media = (n1 + n2) / 2
if media <= 5.0:
    print('Você foi \033[31mREPROVADO\033[m! estude mais.')
elif media > 5.0 and media < 6.9:
    print('Você esta de \033[33mRECUPERAÇAO\033[m.')
elif media > 7.0:
    print('Você foi \033[32mAPROVADO\033[m, Parabens!!!')
#consegui fazer