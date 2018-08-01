# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar
# [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Soma
    [ 2 ] Multiplicação
    [ 3 ] Maior número
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Digite qual opção você deseja: '))
    print('' * 50)
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
        print('' * 50)
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} * {} é {}.'.format(n1, n2, multiplicação))
        print('' * 50)
    elif opção == 3:
        if n1 > n2:
            print('O {} é maior que o {}.'.format(n1, n2))
            print('' * 50)
        else:
            print('O {} é maior que o{}.'.format(n2, n1))
            print('' * 50)
    elif opção == 4:
        print('Selecione novos números: ')
        print('' * 50)
        n1 = float(input('Digite o primeiro valor: '))
        print('' * 50)
        n2 = float(input('Digite o segundo valor: '))
        print('' * 50)
    elif opção == 5:
        print('Programa encerrado.')
        print('' * 50)
    else:
        print('mOpção inválida! Tente novamente: ')
        print('' * 50)



