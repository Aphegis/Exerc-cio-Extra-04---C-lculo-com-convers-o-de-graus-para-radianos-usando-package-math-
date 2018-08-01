#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número inteiro qualquer: ')) #Todo resto da divisão por 2 de um número par será 0
if n % 2 == 0:                                        #Todo resto da divisão por 2 de um número impar será 1
    print('O número {} é par.'.format(n))
else:
    print('O número {} é impar.'.format(n))






