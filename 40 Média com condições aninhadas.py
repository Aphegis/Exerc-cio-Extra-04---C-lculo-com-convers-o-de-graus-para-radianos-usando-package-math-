# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9:
# RECUPERAÇÃO - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
if (nota1 + nota2)/2 >= 7:
    print('O aluno foi \033[1;36maprovado!\033[m')
elif (nota1 + nota2)/2 < 5:
    print('O aluno foi \033[1;31mreprovado!\033[m')
else:
    print('O aluno está em recuperação!')


