#Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar[ 2 ] multiplicar[ 3 ] maior[ 4 ] novos números[ 5 ] sair do programa
n1 = int(input('Digite o Pirmeiro valor: '))
n2 = int(input('Digite o Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('=-=' * 20)
    print('''
    Digite [1] para somar
    Digite [2] para multiplicar
    Digite [3] para maior
    Digite [4] para novos valores
    Digite [5] para sair do programa''')
    print('=-=' * 20)
    opcao = int(input('Oque quer fazer com os valores? '))
    if opcao == 1:
        soma = n1 + n2
        print('\033[32mA soma entre {} e {} é {}\033[m'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicaçao = n1 * n2
        print('\033[32mA multiplicaçao entre {} e {} é {}\033[m'.format(n1, n2, multiplicaçao))
    elif opcao == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[32mO maior numero é o {}\033[m'.format(maior))
    elif opcao == 4:
        n1 = int(input('\033[1;33mDigite o 1ª novo valor:\033[m '))
        n2 = int(input('\033[1;33mDigite o 2ª novo valor:\033[m '))
    elif opcao == 5:
        print('\033[30mFinalizando . . .\033[m')
    else:
        print('\033[31m[ERRO] opçao invalida tente novamente\033[m')
print('\033[35mFim do Programa\033[m')
#consegui