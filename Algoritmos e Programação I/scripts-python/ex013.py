base = 3.8
molho_por_colher = 0.42
molho_por_pizza = molho_por_colher*5
kg_mussarela = 49.90
quant_mussarela = float(input('Quantas gramas de mussarela vão ser usadas na pizza?'))

preco_da_pizza = float(input('Qual o preço da pizza?'))
ingredientes_extras = float(input('Qual o preço dos ingredientes extras?'))

gas_por_pizza = 1.2
embalagem = 0.85

total_da_pizza = base+molho_por_pizza+(quant_mussarela*kg_mussarela)+preco_da_pizza+ingredientes_extras+gas_por_pizza+embalagem
print('O custo total de produção de uma pizza é de R${:.2f}'.format(total_da_pizza))

print('Será pago ao aplicativo de entrega o total de R${:.2f}'.format(total_da_pizza*0.08))

print('Em impostos, será pago o total de R${:.2f}'.format(total_da_pizza*0.12))

print('O valor total é de R${:.2f}.'.format(total_da_pizza+total_da_pizza*0.08+total_da_pizza*0.12))

print('O valor de venda deve ser de R${:.2f}'.format(total_da_pizza+(total_da_pizza/2)))