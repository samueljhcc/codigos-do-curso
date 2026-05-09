# Informações do Paciente:
nome = input('Qual o nome do paciente? ')
idade = int(input('Qual a idade do paciente? '))

# Nível de Prioridade:
gravidade = int(input('Digite o nível de gravidade (0 a 10): '))

# Definição da prioridade:
if gravidade >= 8:
    prioridade = 'Alta prioridade'

elif gravidade >= 5:
    prioridade = 'Média prioridade'

else:
    prioridade = 'Baixa prioridade'

# Aumentar prioridade para idosos:
if idade >= 60:

    if prioridade == 'Baixa prioridade':
        prioridade = 'Média prioridade'

    elif prioridade == 'Média prioridade':
        prioridade = 'Alta prioridade'

print('Prioridade:', prioridade)

# Tempo de Espera:
tempo = int(input('Quantos minutos vai demorar? '))

if tempo >= 120:
    print('Fila muito longa!')
elif tempo < 120 and tempo >= 60:
    print('Fila moderada!')
else:
    print('Fila rápida!')