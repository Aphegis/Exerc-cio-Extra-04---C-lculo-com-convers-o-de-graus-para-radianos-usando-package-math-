# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
# Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: - IMC abaixo
# de 18,5: Abaixo do Peso - Entre 18,5 e 25: Peso Ideal - 25 até 30: Sobrepeso - 30 até
# 40: Obesidade - Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso, seu IMC é de {:.1f}'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal, seu IMC é de {:.1f}'.format(imc))
elif imc == 25 and imc < 30:
    print('Você está com sobrepeso, seu IMC é de {:.1f}'.format(imc))
elif imc == 30 and imc <= 40:
    print('Você está obeso!, seu IMC é de {:.1f}'.format(imc))
else:
    print('Você está com obesidade mórbida, procure ajuda médica!, seu IMC é de {:.1f}'.format(imc))

