# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Desafio 9: Tabuada de um número.

n = int(input('Digite um número: '))
for c in range(1, 11):
    resul = n * c
    print('{} * {} = {}'.format(n, c, resul))



