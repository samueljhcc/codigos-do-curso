porH = float(input('Quanto você ganha por hora?'))
horas = int(input('Quantos horas você trabalha por mês? '))

calc = porH * horas

print('O seu salário bruto esté mês foi de R${:.2f}'.format(calc))
print('Foi pago {:.2f} para o INSS.'.format(calc * 0.08))
print('Foi pago {:.2f} para o sindicato.'.format(calc * 0.05))
print('Foi pago {:.2f} para o Imposto de Renda (IR).'.format(calc * 0.11))

print('Seu salário líquido foi de R${:.2f}'.format(calc - (calc * 0.08) - (calc * 0.05) - (calc * 0.11)))