#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você será multado em R${}, pelo fato de estar a {}Km/h acima dos 80Km/h permitidos.'
          .format((velocidade - 80) * 7, velocidade - 80))
else:
    print('Parabéns! Sua velocidade está dentro do 80km/h previstos por lei.')







