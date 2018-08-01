#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual seu salário? '))
if sal > 1250:
    print('Seu novo salário será de R${:.2f}!'.format(sal * 1.10))
else:
    print('Seu novo salário será de R${:.2f}!'.format(sal * 1.15))
