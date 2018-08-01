#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número entre 0 e 9999: '))  #Método matemático
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('O valor da unidade é: {} \nO valor da dezena é: {} \nO valor da centena é: {} \n'
      'O valor do milhar é: {}'.format(unidade, dezena, centena, milhar))


num = str(int(input('Digite um número entre 0 e 9999: '))+10000)  #Método inteligente (o +10000 é uma soma)
print('unidade...: {} \ndezena....: {} \ncentena...: {} \nmilhar....: {}'.format(num[4], num[3], num[2], num[1]))




