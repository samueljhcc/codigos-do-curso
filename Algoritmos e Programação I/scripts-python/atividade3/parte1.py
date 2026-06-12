# Variáveis para armazenar os gols do mandante e do visitante
from unittest import result


gols_mandante = int(input('Gols do mandante: '))
gols_visitante = int(input('Gols do visitante: '))

# Estrutura para exibir o vencedor ou se houve empate
if gols_mandante > gols_visitante:
    print('Vitória do mandante')
elif gols_mandante < gols_visitante:
    print('Vitória do visitante')
else:
    print('Empate')

# Exibir se foi goleada ou não
diferenca = abs(gols_mandante - gols_visitante)

if diferenca >= 3:
    print('Goleada')