from math import sin, cos, tan, radians
ang = float(input('Digite o \033[1;36mângulo\033[m: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('O valor do seno do ângulo é {:.2f}, o cosseno é de {:.2f} e a tangente é de {:.2f}.'.format(sen, cos, tg))







