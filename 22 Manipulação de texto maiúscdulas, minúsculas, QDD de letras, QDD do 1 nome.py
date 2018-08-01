nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome é: {}, em letras maiúsculas é: {} e em letras minúsculas: {}'.format(nome, nome.upper(), nome.lower()))
print('Seu nome ao todo, com espaços, tem: {} letras.'.format(len(nome)))
print('Seu nome ao todo, sem espaços, tem: {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem: {} letras.'.format(nome.find(' '))) #1º método, não tão bom quanto o 2º.
separado = nome.split()
print('Seu primeiro nome tem: {} letras.'.format(len(separado[0]))) #2º método.

print('Quantidade de letras do seu nome:', len(nome.replace(' ', ''))) #método alternativo.
print('quantidade de letras do primeiro nome:', len(nome.split()[0]))

nome.replace(' ', '')

























































