import random
a1 = input('Digite o nome do primeiro aluno(a): ')
a2 = input('Digite o nome do segundo aluno(a): ')
a3 = input('Digite o nome do terceiro aluno(a): ')
a4 = input('Digite o nome do quarto aluno(a): ')
list = [a1, a2, a3, a4]
escolhido = random.choice(list)
print('\033[1;36mO escolhido foi o(a) {}'.format(escolhido))

