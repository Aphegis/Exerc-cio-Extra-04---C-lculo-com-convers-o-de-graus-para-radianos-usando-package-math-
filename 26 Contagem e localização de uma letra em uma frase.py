#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#  em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase "{}".'.format(frase.lower().count('a'), frase))
print('A letra "A" aparece pela primeira vez na posição de número {}'.format(frase.lower().find('a')+1))
print('A letra "A" aparece pela última vez na posição de número {}'.format(frase.lower().rfind('a')+1))








