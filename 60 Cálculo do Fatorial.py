# Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
num = int(input('Digite um número: '))
fatorial = factorial(num)
print('O fatorial de {} é {}.'.format(num, fatorial))


from math import factorial
num = int(input('Digite um número: '))
c = num # O contador "c" começará com o número "num".
f = 1 # O 1 é o termo neutro da multiplicação, diferente do 0, caso fosse soma/subtração.
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='') # se c for maior que 1 escreva x, senão, escreva "="
    f *= c
    c -= 1
print('O fatorial de {} é {}.'.format(num, f))
