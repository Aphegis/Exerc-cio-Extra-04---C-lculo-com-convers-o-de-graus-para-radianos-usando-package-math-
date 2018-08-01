# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
lista = [0, 10]
print('----- JOGO DA ADVINHAÇÃO! ----')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('Parabéns, você venceu em {} tentativas!'.format(palpites))


