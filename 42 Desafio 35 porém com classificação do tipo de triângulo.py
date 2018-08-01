# Refaça o DESAFIO 035 dos triângulos (condição de existência), acrescentando o recurso de mostrar
# que tipo de triângulo será formado: - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados
# iguais, um diferente - ESCALENO: todos os lados diferentes

l1 = float(input('Digite o comprimento do primeiro lado do triângulo: '))
l2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
l3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))
if l2 + l3 > l1 and l2 + l1 > l3 and l1 + l2 > l3:
    print('O triângulo \033[1;34mexiste\033[m', end='')
    if l1 == l2 and l1 == l3:
        print(' e é equilátero.')
    elif l1 != l2 and l1 != l3:
        print(' e é escaleno.')
    elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
        print(' e é isósceles.') # Essa parte do isósceles dá pra por apenas um "else:"
else:
    print('O triângulo \033[1;31mnão\033[m existe.')

