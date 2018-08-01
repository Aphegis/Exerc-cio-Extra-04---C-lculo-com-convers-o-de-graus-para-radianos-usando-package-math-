# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
1 - PEDRA
2 - PAPEL
3 - TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('JO')
sleep(1)
print('KEN')
sleep(0.8)
print('PO!!')
sleep(0.5)
if computador == 0:
    if jogador == 0:
        print('Empate.')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Jogada inválida!')



