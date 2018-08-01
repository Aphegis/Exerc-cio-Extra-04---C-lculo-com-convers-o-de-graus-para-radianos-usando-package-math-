import math
CO = float(input('Digite o valor do cateto oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))
Hip = math.hypot(CO, CA)
print('O valor da hipotenusa é {:.0f}'.format(Hip))
