# MISSÃO ARES-7 PARA MARTE #
# SISTEMA DE GERENCIAMENTO DE RECURSOS #

# LISTAS PARA OS TRIPULANTES
tripulantes = []
funcoes = []
consumo_total = []

# DEFINIÇÃO DOS ESTOQUES
estoques_definidos = False

# ESTOQUES INICIAIS
oxigenio_inicial = 0
agua_inicial = 0
alimento_inicial = 0
energia_inicial = 0

# ESTOQUES
oxigenio = 0
agua = 0
alimento = 0
energia = 0

# DIAS CORRIDOS
dias = 0

# DEFINIÇÃO DO MENU E INÍCIO DA ESTRUTURA DE REPETIÇÃO
while True:

    # MENU DO SISTEMA
    print('========= MISSÃO ARES-7 ========')
    print('1 - Cadastrar tripulantes')
    print('2 - Definir estoques iniciais')
    print('3 - Registrar consumo diário')
    print('4 - Ver percentual restante')
    print('5 - Ver projeção da missão')
    print('6 - Ver maior e menor consumidor')
    print('0 - Encerrar sistema')
    print('================================')

    opcao = input('escolha uma opção: ')

    # OPÇÃO 1 - CADASTRAR TRIPULANTES #
    if opcao == "1":
        if len(tripulantes) > 0:
            print('Tripulantes já cadastrados!')
        else:
            qtd = int(input('Quantos tripulantes deseja cadastrar? (1 até 10): '))

            # VALIDAÇÃO
            while qtd < 0 or qtd > 10:
                print('Quantidade inválida. Digite um número entre 1 e 10: ')
                qtd = int(input('Quantos tripulantes deseja cadastrar? (1 até 10): '))

            # CADASTRO DE TRIPULANTES
            for i in range(qtd):
                nome = input(f'Qual o nome do tripulante {i + 1}? ')
                funcao = input(f'Qual a função do tripulante? (ex: Engenheiro, Médico, Piloto etc.): ')

                tripulantes.append(nome)
                funcoes.append(funcao)
            
                consumo_total.append(0)

            print('Tripulantes cadastrados com sucesso!')

    # OPÇÃO 2 - DEFINIR ESTOQUES INICIAIS #
    elif opcao == '2':
        if estoques_definidos:
            print('Estoques já definidos!')

        # DEFINIÇÃO DE ESTOQUES    
        else:

            # OXIGÊNIO
            oxigenio = float(input('Oxigênio (litros): '))
            while oxigenio <= 0:
                oxigenio = float(input('Digite um valor maior que zero: '))
            
            # ÁGUA
            agua = float(input('Água (litros): '))
            while agua <= 0:
                agua = float(input('Digite um valor maior que zero: '))

            # ALIMENTO
            alimento = float(input('Alimento (kg): '))
            while alimento <= 0:
                alimento = float(input('Digite um valor maior que zero: '))

            # ENERGIA
            energia = float(input('Energia (kWh): '))
            while energia <= 0:
                energia = float(input('Digite um valor maior que zero: '))

            oxigenio_inicial = oxigenio
            agua_inicial = agua
            alimento_inicial = alimento
            energia_inicial = energia

            estoques_definidos = True

            print('Estoques iniciais definidos com sucesso!')

    # OPÇÃO 3 - REGISTAR CONSUMO DIÁRIO #
    elif opcao == '3':
        if len(tripulantes) == 0:
            print('Cadastre os tripulantes primeiro!')
        elif estoques_definidos == False:
            print('Defina os estoques iniciais primeiro!')
        else:

            # QUANTIDADE DE TRIPULANTES PARA REGISTRAR O CONSUMO
            for i in range(len(tripulantes)):

                print(f'\nTripulante: {tripulantes[i]}')

                # OXIGÊNIO
                consumo_oxigenio = float(input('Consumo de oxigênio:'))
                while consumo_oxigenio < 0 or consumo_oxigenio > oxigenio:
                    print('Valor inválido!')
                    consumo_oxigenio = float(input('Digite novamente:'))

                oxigenio -= consumo_oxigenio

                # ÁGUA
                consumo_agua = float(input('Consumo de água: '))
                while consumo_agua < 0 or consumo_agua > agua:
                    print('Valor inválido!')
                    consumo_agua = float(input('Digite novamente:'))

                agua -= consumo_agua

                # ALIMENTO
                consumo_alimento = float(input('Consumo de alimento: '))
                while consumo_alimento < 0 or consumo_alimento > alimento:
                    print('Valor inválido!')
                    consumo_alimento = float(input('Digite novamente: '))   

                alimento -= consumo_alimento

                # ENERGIA
                consumo_energia = float(input('Consumo de energia: '))
                while consumo_energia < 0 or consumo_energia > energia:
                    print('Valor inválido!')
                    consumo_energia = float(input('Digite novamente: '))

                energia -= consumo_energia

                total = (
                    consumo_oxigenio
                    + consumo_agua
                    + consumo_alimento
                    + consumo_energia
                )

                # CONSUMO DE CADA TRIPULANTE
                consumo_total[i] += total

            dias += 1

            print('Consumo diário registrado com sucesso!')