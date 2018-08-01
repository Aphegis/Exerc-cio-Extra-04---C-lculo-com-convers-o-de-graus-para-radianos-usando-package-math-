from random import shuffle
a1 = input('Nome do primeiro aluno(a): ')
a2 = input('Nome do segundo aluno(a): ')
a3 = input('Nome do terceiro aluno(a): ')
a4 = input('Nome do quarto aluno(a): ')
lista= [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: \033[4;36m{}'.format(lista))
