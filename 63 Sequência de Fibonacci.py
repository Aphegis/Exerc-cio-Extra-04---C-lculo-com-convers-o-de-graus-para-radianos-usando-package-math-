# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de
# uma Sequência de Fibonacci. Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 (a1 + a2 = a3 | a2 + a3 = a4 | a3 + a4 = a5...

a1 = 0
a2 = 1
n = int(input('Digite o número de termos: '))
cont = 3
print('{} {}'.format(a1, a2), end=' ')
while cont <= n:
    a3 = a2 + a1
    print('{}'.format(a3), end=' ')
    cont += 1
    a1 = a2
    a2 = a3
