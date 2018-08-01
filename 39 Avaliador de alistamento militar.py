# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se
# ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('Digite o ano de seu nascimento: '))
hoje = date.today().year
if hoje - nascimento == 18:
    print('O ano de {} é o ano exato em que você terá que se alistar!'.format(date.today().year))
elif hoje - nascimento > 18:
    print('O momento de seu alistamento já passou! Ele ocorreu em {}.'.format(nascimento + 18))
else:
    print('O momento de seu alistamento ainda não chegou! Ele ocorrerá em {}.'.format(nascimento +18))

