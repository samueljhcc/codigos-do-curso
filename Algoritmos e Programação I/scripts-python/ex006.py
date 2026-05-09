# Leia a leitura inicial e a leitura final de uma bomba de combustível (em litros) e o preço por litro praticado.
# Calcule a quantidade total de litros vendidos e o faturamento bruto da bomba.
# Sabendo que o custo de aquisição do combustível representa 72% do preço de venda, calcule também o lucro bruto.

inicial = float(input('Qual a leitura inicial? '))
final = float(input('Qual a leitura final? '))
preco = float(input('Quanto custa o litro da gasolina? R$' ))

quant = float(input('Quantos litros foram vendidos?'))
faturamento_bruto = preco*quant
print('O faturamento bruto é: R${:.2f}'.format(faturamento_bruto))

lucro_bruto = faturamento_bruto*0.28
print('O lucro bruto é de: R${:.2f}'.format(lucro_bruto))