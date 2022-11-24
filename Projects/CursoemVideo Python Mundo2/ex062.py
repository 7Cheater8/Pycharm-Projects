#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos
numero = int(input('Digite o rimeiro Termo: '))
razao = int(input('Digite a Razao: '))
termo = numero
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Qauntos termos voce que mostrar a mais?'))
print ('Progressaão finalizada com {} termos mostrados'.format(total))
