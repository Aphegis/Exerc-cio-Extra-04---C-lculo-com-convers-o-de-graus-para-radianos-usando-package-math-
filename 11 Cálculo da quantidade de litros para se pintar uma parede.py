print('Bem-vindo à ferramenta para previsão do gasto de litros de tinta em pinturas de paredes.')
base = int(input('Digite o comprimento da base da parede: '))
altura = int(input('Digite a altura da parede: '))
tinta = int(input('Digite quantos metros quadrados um litro de tinta é capaz de pintar: '))
área = base*altura
print('A área desta parede é de {} e a quantidade necessária de litros para a total pintura é '
      'de {} litros.'.format(área, área/tinta))
