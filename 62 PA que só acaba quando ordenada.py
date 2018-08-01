# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar 0 termos.

primeiro = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
print('A progressão aritmética que possui o primeiro termo {} e a razão {} terá os seguinte '
      'valores: '.format(primeiro, razao))
while mais != 0:
    total += mais
    while cont <= total:
        print(primeiro, end=' ')
        cont += 1
        primeiro += razao
    mais = int(input('\nQuantos termos a mais você desejar mostrar? '))
print('PA finalizada com {} termos no total.'.format(total))






