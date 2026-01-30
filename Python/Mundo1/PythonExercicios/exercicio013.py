salario = float(input('Insira o valor do salário do funcionário: '))
aumento = salario*(15/100)
novo_salario = salario + aumento
print('O novo salário do funcionário vai ser de R${:.2f}, um aumento de R${:.2f}'.format(novo_salario, aumento))
