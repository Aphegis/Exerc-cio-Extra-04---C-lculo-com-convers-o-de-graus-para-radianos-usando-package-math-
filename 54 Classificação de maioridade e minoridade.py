# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date
menor = 0
maior = 0
for c in range(0,  7):
    nasc = int(input('Digite o ano de seu nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas {} são de maior e {} de menor.'.format(menor, maior))

