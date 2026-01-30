real = float(input('Quantos reais você tem na carteira?(Ex: 5.40): '))
dolar = real / 5.23
print('Com base na cotação atual do dólar, com R${}, você consegue comprar US${:.2f}'.format(real, dolar))