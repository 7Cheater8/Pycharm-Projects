#Desenvolva uma logica que leia o peso e a autura de uma pessoa caucule seu imc e mostre seu stauts, de acordo com a tabela abaixo: <= 18.5 abaixo do peso, 18.5 a 25: peso ideal, 25 a 30: sobrepeso, 30 a 40 obesidade, acima de 40 obesiadde morbida
peso = int(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
cores = {'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'roxo': '\033[35m'}
if imc <= 18.5:
    print('Com {:.1f} de IMC voce esta {}Abaixo do peso ▼'.format(imc, cores['vermelho']))
elif imc <= 25:
    print('Com {:.1f} de IMC voce esta {}Peso ideal ☻'.format(imc, cores['verde']))
elif imc <= 30:
    print('Com {:.1f} de IMC voce esta {}Sobrepeso ▲'.format(imc, cores['amarelo']))
elif imc <= 40:
    print('Com {:.1f} de IMC voce esta {}Obesidade ▲▲'.format(imc, cores['azul']))
else:
    print('Com {:.1f} de IMC voce esta {}Obesidade Morbida ▬▬'.format(imc, cores['roxo']))
#consegui fazer sozinho ☻