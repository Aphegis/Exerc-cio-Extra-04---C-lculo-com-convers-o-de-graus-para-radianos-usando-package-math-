# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

#está o num = int pois dessa forma o código não soma o 999, guanabara não explicou o porquê, pois na aula 15 resolverá
num = cont = soma = 0
num = int(input('Digite valores para serem somados [ 999 ] - Condição de parada: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite valores para serem somados [ 999 ] - Condição de parada: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
