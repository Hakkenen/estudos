n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n multiplicação vale {},\n divisão vale {:.3}'.format(s, m, d), end=' ')
print('Divisão inteira vale {}, potenciação vale {}'.format(di,e))
