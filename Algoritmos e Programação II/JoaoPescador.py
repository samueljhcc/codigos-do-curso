peso = float(input('Digite o peso dos peixes em kg: '))
excesso = peso - 50
multa = excesso * 4

if peso > 50:
    print('O peso excedeu o limite de 50kg.')
    print('O excesso de peso é de {:.2f}kg'.format(excesso))
    print('A multa a ser paga é de R${:.2f}'.format(multa))
elif peso == 50:
    print('O peso está exatamente no limite de 50kg.')
else:
    print('O peso não atingiu o limite de 50kg. Não há excesso nem multa a ser paga.')
