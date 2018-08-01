# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10
# até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('Os fogos comecarão a estourar em 10 segundos!')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('Contagem finalizada, os fogos estão estourando!')
