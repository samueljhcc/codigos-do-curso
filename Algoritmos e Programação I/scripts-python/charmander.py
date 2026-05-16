n1 = int(input('Qual o nível atual do Charmander? '))
n2 = int(input('Qual o nível que o treinador deseja alcançar? '))

while n1 < n2:
    print('Nível atual: {}'.format(n1))
    print('Treinando...')
    n1 += 1
else:
    print('Novo nível alcançado: {}'.format(n1))
    print('Parabéns, o Charmander evoluiu para Charmeleon! O nível dele agora é {}'.format(n1))