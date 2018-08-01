# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Palíndromo = Se lida de trás pra frente é idêntica à leitura normal.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print('É políndromo.')
else:
    print('Não é políndromo.')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]            #Método 2 sem o "for".
if inverso == junto:
    print('É políndromo.')
else:
    print('Não é políndromo.')
