from math import ceil

area = float(input('Digite o tamanho da área em metros quadrados: '))

litros = area / 3
latas = ceil(litros / 18)
preco = latas * 80

print('Você vai precisar de {} latas de tinta.'.format(latas))
print('O preço total vai ser de R${:.2f}'.format(preco))