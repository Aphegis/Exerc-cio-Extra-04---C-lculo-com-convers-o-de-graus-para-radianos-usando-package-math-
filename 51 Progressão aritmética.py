# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

a1 = float(input('Digite o primeiro termo da progressão aritmética: '))
r = float(input('Digite a razão da progressão aritmética: '))
print('Os 10 primeiros termos da PA de primeiro termo {} e razão {}'
          ' são: '.format(a1, r))
for n in range(0, 10):
    print(a1 + (r * n), end=' ')



