# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n1 = int(input('Digite um valor: '))
total = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
if total == 2:
    print('\n\033[mÉ primo.')
else:
    print('\n\033[mNão é primo.')



