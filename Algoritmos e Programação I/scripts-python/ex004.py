litros = int(input('Quantos litros deseja pagar: '))
GASOLINA = 3.85

sem_desconto = litros*GASOLINA
print('O valor sem desconto é: R${}'.format(sem_desconto))
desconto = sem_desconto*0.04
print('O valor do desconto é: R${:.2f}'.format(desconto))
total = sem_desconto-desconto
print('O valor total a ser pago é: R${:.2f}'.format(total))