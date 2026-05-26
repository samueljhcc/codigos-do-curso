PAO = 0.75

total = 0

p = int(input('Quantos pães o cliente vai querer? '))

while p != 0:

    valor = PAO * p

    if p > 10:
        desconto = valor * 0.10
        valor = valor - desconto

    print('Valor que o cliente deve pagar: R${:.2f}'.format(valor))

    total = total + valor

    p = int(input('Quantos pães o próximo cliente vai querer?'))


print('O valor total arracadado é de: R${:.2f}'.format(total))