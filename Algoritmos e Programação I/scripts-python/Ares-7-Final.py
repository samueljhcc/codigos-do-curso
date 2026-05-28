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
            oxigenio = float(input('Oxigênio (litros): '))
            while oxigenio <= 0:
                oxigenio = float(input('Digite um valor maior que zero: '))
                
            agua = float(input('Água (litros): '))
            while agua <= 0:
                agua = float(input('Digite um valor maior que zero: '))

            alimento = float(input('Alimento (kg): '))
            while alimento <= 0:
                alimento = float(input('Digite um valor maior que zero: '))

            energia = float(input('Energia (kWh): '))
            while energia <= 0:
                energia = float(input('Digite um valor maior que zero: '))

            oxigenio_inicial = oxigenio
            agua_inicial = agua
            alimento_inicial = alimento
            energia_inicial = energia

            estoques_definidos = True

            print('Estoques iniciais definidos com sucesso!')