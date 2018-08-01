# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.

vcasa = float(input('Digite o valor da casa: R$ '))
scomprador = float(input('Digite o salário do comprador: R$ '))
qanos = float(input('Digite a quantidade de anos que durará o pagamento: '))
pmensal = vcasa / (qanos * 12)
porcentagem = pmensal * 100 / scomprador
if pmensal <= 0.3 * scomprador:
    print('O valor do pagamento mensal de tal imóvel é de R${:.2f}.\nPara o empréstimo ser aprovado o pagamento mensal'
          ' não deve ser superior a 30% do salário do indivíduo. O resultado foi: {:.2f}%\nSeu empréstimo foi '
          '\033[1;32maceito\033[m, parabéns!'.format(pmensal, porcentagem))


else:
    print('O valor do pagamento mensal de tal imóvel é de R${:.2f}.\nPara o empréstimo ser aprovado o pagamento mensal'
          ' não deve ser superior a 30% do salário do indivíduo. O resultado foi: {:.2f}%\nO empréstimo '
          '\033[1;31mnão é viável\033[m, desculpe.'.format(pmensal, porcentagem))




