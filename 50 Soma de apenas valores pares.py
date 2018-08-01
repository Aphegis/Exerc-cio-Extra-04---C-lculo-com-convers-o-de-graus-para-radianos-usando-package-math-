# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o
# valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for num in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('O resultado da soma dos números pares é {} e o total de números pares {}.'.format(soma, cont))



