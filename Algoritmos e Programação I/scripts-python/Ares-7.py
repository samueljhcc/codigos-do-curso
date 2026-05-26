# MISSÃO ARES-7 PARA MARTE
# Sistema de Monitoramento de Recursos

# -----------------------------
# LISTAS DOS TRIPULANTES
# -----------------------------
nomes = []
funcoes = []
consumo_total = []

# -----------------------------
# VARIÁVEIS DOS ESTOQUES
# -----------------------------
estoques_definidos = False

oxigenio = 0
agua = 0
alimento = 0
energia = 0

# Estoques iniciais (para cálculos futuros)
oxigenio_inicial = 0
agua_inicial = 0
alimento_inicial = 0
energia_inicial = 0

# Controle de dias simulados
dias = 0


# MENU PRINCIPAL
while True:

    print("========= MISSÃO ARES-7 =========")
    print("1 - Cadastrar tripulantes")
    print("2 - Definir estoques iniciais")
    print("3 - Registrar consumo diário")
    print("4 - Ver percentual restante")
    print("5 - Ver projeção da missão")
    print("6 - Ver maior e menor consumidor")
    print("0 - Encerrar")
    print("=================================")

    opcao = input("Escolha uma opção: ")

    # ==========================================
    # OPÇÃO 1 - CADASTRAR TRIPULANTES
    # ==========================================
    if opcao == "1":

        # Verifica se já existem tripulantes
        if len(nomes) > 0:
            print("Tripulantes já cadastrados!")
        else:

            qtd = int(input("Quantos tripulantes? (1 até 10): "))

            # Validação
            while qtd < 1 or qtd > 10:
                qtd = int(input("Valor inválido! Digite entre 1 e 10: "))

            # Cadastro
            for i in range(qtd):

                nome = input(f"Nome do tripulante {i+1}: ")
                funcao = input("Função: ")

                nomes.append(nome)
                funcoes.append(funcao)

                # Consumo começa em zero
                consumo_total.append(0)

            print("Tripulantes cadastrados com sucesso!")

    # ==========================================
    # OPÇÃO 2 - DEFINIR ESTOQUES
    # ==========================================
    elif opcao == "2":

        if estoques_definidos:
            print("Estoques já definidos!")
        else:

            # Entrada dos valores
            oxigenio = float(input("Oxigênio (litros): "))
            while oxigenio <= 0:
                oxigenio = float(input("Digite um valor maior que zero: "))

            agua = float(input("Água (litros): "))
            while agua <= 0:
                agua = float(input("Digite um valor maior que zero: "))

            alimento = float(input("Alimentos (kg): "))
            while alimento <= 0:
                alimento = float(input("Digite um valor maior que zero: "))

            energia = float(input("Energia (kWh): "))
            while energia <= 0:
                energia = float(input("Digite um valor maior que zero: "))

            # Guardando os valores iniciais
            oxigenio_inicial = oxigenio
            agua_inicial = agua
            alimento_inicial = alimento
            energia_inicial = energia

            estoques_definidos = True

            print("Estoques definidos com sucesso!")

    # ==========================================
    # OPÇÃO 3 - CONSUMO DIÁRIO
    # ==========================================
    elif opcao == "3":

        # Verificações
        if len(nomes) == 0:
            print("Cadastre os tripulantes primeiro!")

        elif not estoques_definidos:
            print("Defina os estoques primeiro!")

        else:

            # Percorre todos os tripulantes
            for i in range(len(nomes)):

                print(f"\nTripulante: {nomes[i]}")

                # ---------------- OXIGÊNIO ----------------
                consumo_oxigenio = float(input("Consumo de oxigênio: "))

                while consumo_oxigenio < 0 or consumo_oxigenio > oxigenio:
                    print("Valor inválido!")
                    consumo_oxigenio = float(input("Digite novamente: "))

                oxigenio -= consumo_oxigenio

                # ---------------- ÁGUA ----------------
                consumo_agua = float(input("Consumo de água: "))

                while consumo_agua < 0 or consumo_agua > agua:
                    print("Valor inválido!")
                    consumo_agua = float(input("Digite novamente: "))

                agua -= consumo_agua

                # ---------------- ALIMENTO ----------------
                consumo_alimento = float(input("Consumo de alimento: "))

                while consumo_alimento < 0 or consumo_alimento > alimento:
                    print("Valor inválido!")
                    consumo_alimento = float(input("Digite novamente: "))

                alimento -= consumo_alimento

                # ---------------- ENERGIA ----------------
                consumo_energia = float(input("Consumo de energia: "))

                while consumo_energia < 0 or consumo_energia > energia:
                    print("Valor inválido!")
                    consumo_energia = float(input("Digite novamente: "))

                energia -= consumo_energia

                # Soma total do dia
                total = (
                    consumo_oxigenio
                    + consumo_agua
                    + consumo_alimento
                    + consumo_energia
                )

                # Acumula o consumo do tripulante
                consumo_total[i] += total

            # Incrementa 1 dia
            dias += 1

            print("\nConsumo diário registrado!")

    # ==========================================
    # OPÇÃO 4 - PERCENTUAL RESTANTE + ALERTA
    # ==========================================
    elif opcao == "4":

        if not estoques_definidos:
            print("Defina os estoques primeiro!")

        else:

            # Cálculo dos percentuais
            porcent_oxigenio = (oxigenio / oxigenio_inicial) * 100
            porcent_agua = (agua / agua_inicial) * 100
            porcent_alimento = (alimento / alimento_inicial) * 100
            porcent_energia = (energia / energia_inicial) * 100

            # Função para alerta
            def status(valor):
                if valor < 20:
                    return "ALERTA"
                else:
                    return "OK"

            # Exibição
            print("\n===== PERCENTUAL RESTANTE =====")

            print(f"Oxigênio: {porcent_oxigenio:.2f}% - {status(porcent_oxigenio)}")
            print(f"Água: {porcent_agua:.2f}% - {status(porcent_agua)}")
            print(f"Alimento: {porcent_alimento:.2f}% - {status(porcent_alimento)}")
            print(f"Energia: {porcent_energia:.2f}% - {status(porcent_energia)}")

    # ==========================================
    # OPÇÃO 5 - PROJEÇÃO DA MISSÃO
    # ==========================================
    elif opcao == "5":

        if dias == 0:
            print("Simule pelo menos 1 dia!")
        else:

            # Consumo médio por dia
            media_oxigenio = (oxigenio_inicial - oxigenio) / dias
            media_agua = (agua_inicial - agua) / dias
            media_alimento = (alimento_inicial - alimento) / dias
            media_energia = (energia_inicial - energia) / dias

            print("\n===== PROJEÇÃO =====")

            # Lista para verificar viabilidade
            dias_restantes_lista = []

            # Função para projeção
            def projecao(estoque, media, nome):

                if media == 0:
                    print(f"{nome}: Infinito (sem consumo)")
                    dias_restantes_lista.append(999999)

                else:
                    dias_restantes = estoque / media
                    dias_restantes_lista.append(dias_restantes)

                    print(f"{nome}: {dias_restantes:.2f} dias restantes")

            # Chamadas
            projecao(oxigenio, media_oxigenio, "Oxigênio")
            projecao(agua, media_agua, "Água")
            projecao(alimento, media_alimento, "Alimento")
            projecao(energia, media_energia, "Energia")

            # --------------------------------
            # VERIFICAR VIABILIDADE
            # --------------------------------

            recursos = ["Oxigênio", "Água", "Alimento", "Energia"]

            viavel = True
            gargalo = ""

            for i in range(len(dias_restantes_lista)):

                total_dias = dias + dias_restantes_lista[i]

                if total_dias < 210:
                    viavel = False
                    gargalo = recursos[i]
                    break

            print("\n===== VIABILIDADE =====")

            if viavel:
                print("MISSÃO VIÁVEL")
            else:
                print("MISSÃO INVIÁVEL")
                print("Recurso crítico:", gargalo)

    # ==========================================
    # OPÇÃO 6 - MAIOR E MENOR CONSUMIDOR
    # ==========================================
    elif opcao == "6":

        if dias == 0:
            print("Simule pelo menos 1 dia!")

        else:

            # Maior e menor consumo
            maior = max(consumo_total)
            menor = min(consumo_total)

            print("\n===== MAIOR CONSUMIDOR =====")

            # Verifica empates
            for i in range(len(consumo_total)):
                if consumo_total[i] == maior:
                    print(f"{nomes[i]} -> {maior:.2f}")

            print("\n===== MENOR CONSUMIDOR =====")

            for i in range(len(consumo_total)):
                if consumo_total[i] == menor:
                    print(f"{nomes[i]} -> {menor:.2f}")

    # ==========================================
    # OPÇÃO 0 - SAIR
    # ==========================================
    elif opcao == "0":

        print("Sistema encerrado.")
        break

    # ==========================================
    # OPÇÃO INVÁLIDA
    # ==========================================
    else:
        print("Opção inválida!")