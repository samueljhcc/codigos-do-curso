combustivel = float(input('Quanto foi vendido no dia? R$'))
comissao = combustivel*0.015
DIARIA = 85

total = comissao + DIARIA

print('O valor total a ser recebido é de R${:.2f}'.format(total))