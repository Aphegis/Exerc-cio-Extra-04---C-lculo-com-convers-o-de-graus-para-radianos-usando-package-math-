# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

a1 = float(input('Digite o primeiro termo da progressão aritmética: '))
r = float(input('Digite a razão da progressão aritmética: '))
print('Os 10 primeiros termos da progressão artimética de primeiro termo {} e razão {} é: '.format(a1, r))
termo = a1
cont = 1
while cont <= 10:
    print(termo, end=' ')
    termo += 1
    cont += 1


