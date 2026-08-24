tamanho = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade de download em Mbps: '))

calc = tamanho / velocidade
converter = calc / 60

print('O tempo de download será de aproximadamente {:.2f} minutos.'.format(converter))