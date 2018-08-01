#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu nome completo é {}, seu primeiro nome {}'
      ' e seu último nome {}.'.format(nome, dividido[0], dividido[len(dividido)-1]))

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu último nome é {}'.format(dividido[-1])) # <--- modo melhor é com o -1





