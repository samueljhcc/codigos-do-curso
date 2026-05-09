# Informações do Paciente:
nome = input('Qual o nome do paciente? ')
idade = int(input('Qual a idade do paciente? '))

# Nível de Prioridade:
prioridade = int(input('De 0 a 10, qual a graviddae do estado do paciente?'))

if prioridade >= 8:
    print('Alta Prioridade!')
elif prioridade >= 5 and prioridade <= 7:
    print('Média Prioridade!')
elif prioridade >= 5 and prioridade <= 7 and idade >= 60:
    print('Alta Prioridade!')
elif prioridade > 5:
    print('Baixa Prioridade!')
else:
    print('Não é Prioridade!')

# Tempo de Espera:
tempo = int(input('Quantos minutos vai demorar? '))

if tempo >= 120:
    print('Fila muito longa!')
elif tempo < 120 and tempo >= 60:
    print('Fila moderada!')
else:
    print('Fila rápida')