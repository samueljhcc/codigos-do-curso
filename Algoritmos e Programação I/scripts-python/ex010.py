largura = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))
area = largura * altura

custo = area*25

print('A altura da largura é de {}m, a altura é de {}m, e o custo da pintura vai ser de R${:.2f}'.format(largura, altura, custo))