inicio = 'Programa de orçamento para pintura'
print('{:=^50}'.format(inicio))
largura = float(input('Insira a largura da parede em metros(ex: 3.40): '))
altura = float(input('Insira a altura da parede em metros (ex: 2.50): '))
area = largura*altura
tinta = area/2
print('A área em m² da parede é: {} e para pintar a parede você precisa de {} Litros de tinta'.format(area, tinta))