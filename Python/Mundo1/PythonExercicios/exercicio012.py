inicio = 'Calculadora de desconto'
print('{:=^50}'.format(inicio))
preco = float(input('Insira o valor do produto(ex:4.99):'))
valordesconto = preco*(5/100)
precodesconto = preco - valordesconto
print('O valor do produto com desconto de 5% é de:R${:.2f}. Um desconto de R${:.2f}'.format(precodesconto, valordesconto))
