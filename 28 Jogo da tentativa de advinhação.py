#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import random
from time import sleep
list = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(list)
digitado = int(input('Tente descobrir um número entre 0 e 5: '))
print('Analisando...')
sleep(1)
if digitado == escolhido:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! O computador pensou no número {} e não no {}.'.format(escolhido, digitado))













