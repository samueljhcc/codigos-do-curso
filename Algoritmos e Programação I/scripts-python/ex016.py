quant = int(input('Quantos pães o cliente vai querer? '))

while quant != 0:

    if quant > 11:
        print('O cliente deve pegar R${:.2f}'.format((quant*0.75)*0.9))
        quant = int(input('Quantos pães o cliente vai querer? '))
    else:
        print('O cliente deve pagar R${:.2f}'.format(quant*0.75))
        quant = int(input('Quantos pães o cliente vai querer? '))