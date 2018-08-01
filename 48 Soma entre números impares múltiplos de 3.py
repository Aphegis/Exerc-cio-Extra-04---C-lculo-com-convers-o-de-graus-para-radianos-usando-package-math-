# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.

cont = 0
soma = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        soma += c
        cont += 1
print('A soma é {} e o número de valores é {}.'.format(soma, cont, end=' '))

