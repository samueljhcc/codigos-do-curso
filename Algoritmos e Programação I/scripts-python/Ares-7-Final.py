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