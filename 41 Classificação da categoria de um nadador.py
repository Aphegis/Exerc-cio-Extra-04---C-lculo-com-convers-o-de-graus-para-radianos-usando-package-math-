# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM - Até
# 14 anos: INFANTIL - Até 19 anos: JÚNIOR - Até 25 anos: SÊNIOR - Acima de 25 anos: MASTER

from datetime import date
idade = int(input('Digite sua idade ou ano de nascimento: '))
anoatual = date.today().year
idade2 = anoatual - idade
if idade <= 9 or idade2 <= 9:
    print('A categoria adequada é a "mirim".')
elif idade <= 14 or idade2 <= 14:
    print('A categoria adequada é a "infantil".')
elif idade <= 19 or idade2 <= 19:
    print('A categoria adequada é a "júnior".')
elif idade <= 25 or idade2 <= 25:
    print('A categoria adequada é a "sênior')
elif idade > 25:
    print('A categoria adequada é a "master"')
