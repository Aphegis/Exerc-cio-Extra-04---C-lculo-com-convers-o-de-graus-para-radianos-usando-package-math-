dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos no total? '))
Pdias = dias * 60
Pkm = 0.15 * km
Ptotal = Pdias + Pkm
print('O valor total a ser pago é de R${:.2f}'.format(Ptotal))




