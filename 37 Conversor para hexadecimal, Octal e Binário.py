# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número para ser convertido: '))
escolhido = int(input('Escolha qual tipo de conversão:\n[ 1 ] Para binário \n[ 2 ] '
                      'Para Octal \n[ 3 ] Para Hexadecimal \nDigite aqui: '))
if escolhido == 1:
    print('A conversão de {} para binário é: {}'.format(num, bin(num)[2:]))
elif escolhido == 2:
    print('A conversão de {} para Octal é: {}'.format(num, oct(num)[2:]))
elif escolhido == 3:
    print('A conversão de {} para Hexadecimal é: {}'.format(num, hex(num)[2:]))


