empate = 0
v_casa = 0
v_visitante = 0

for i in range(5):
    casa = int(input('Digite o número de gols do time da casa: '))
    visitante = int(input('Digite o número de gols do time visitante: '))
    if casa > visitante:
        print('Vitória do time da casa!')
        v_casa += 1
    elif visitante > casa:
        print('Vitória do time visitante!')
        v_visitante += 1
    else:
        print('Empate!')
        empate += 1

print('O número de vitórias do time da casa foi {}.'.format(v_casa))
print('O número de vitórias do time visitante foi {}.'.format(v_visitante))
print('O número de empates foi {}.'.format(empate))