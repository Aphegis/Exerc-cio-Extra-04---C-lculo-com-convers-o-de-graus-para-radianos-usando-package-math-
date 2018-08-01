#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior valor digitado foi o {} e o menor {}.'.format(maior, menor))


primeiro = int(input('Digite o primeiro número:'))  #Melhor modo
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]
print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))


