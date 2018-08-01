# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de
# desconto - em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' Lojas Farine '))
preço = float(input('Digite o preço do produto: '))
metodo = int(input('Escolha o método de pagamento:\n[ 1 ] - À vista. 5% de desconto.\n[ 2 ] - Em até 2x'
                   ' no cartão. Preço formal.\n[ 3 ] - 3x ou mais no cartão. 20% de juros.'
                   '\nDigite aqui: '))
if metodo == 1:
    print('O valor do produto receberá 5% de desconto, totalizando: R${:.2f}'.format(preço * 0.95))
elif metodo == 2:
    print('O valor do produto poderá ser parcelado em 2 vezes sem alteração no valor'
          ' ,totalizando: R${:.2f} e cada parcela custando: R${:.2f}'.format(preço, preço/2))
else:
    nvezes = int(input('Digite o número de parcelas (minímo: 3, máximo: 12): '))
    if nvezes < 3 or nvezes > 12:
        print('Tal número de meses \033[1;31mNÂO\033[m é permitido!')
    else:
        print('O valor do produto será parcelado em {} vezes, o preço total sofrerá juros de'
              ' 20%, fazendo com que cada parcela custe: R${:.2f}, \ne o total a ser pago: R${:.2f}'
              .format(nvezes, (preço / nvezes) * 1.2, preço * 1.2))





