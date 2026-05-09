horas = float(input('Quantas horas por dia ele vai caminhar?'))
dias = int(input('Quantas dias vai levar?'))

oxigenio = (72*60)*0.85
quant_cilin = round((oxigenio/640)+1)
peso_cilin = quant_cilin*4.2

cal_caminhando = (horas*3)*420
horas_descansando = ((dias*24)-(horas*3))
cal_descansando = horas_descansando*70
total_cal = cal_caminhando+cal_descansando

barras = (total_cal/280)+1
total_barras = round(barras)
peso_barras = total_barras*0.065

print('Será consumido o total de {}L de oxigênio.'.format(oxigenio))
print('Serão necessários {} cilindros de oxigênio.'. format(quant_cilin))
print('Serão necessárias {} calorias.'.format(total_cal))
print('Serão necessárias {} barras energéticas.'.format(total_barras))
print('Será carregado o total de {:.2f}kg.'.format(peso_cilin+peso_barras))