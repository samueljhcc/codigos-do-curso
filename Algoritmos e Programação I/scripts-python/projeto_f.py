# ============================================================
#   OLIMPÍADA INTERNA DE PROGRAMAÇÃO — Sistema de Placar
# ============================================================

# ---------- DADOS GLOBAIS ----------
times = {}          # { nome_time: [membro1, membro2, membro3] }
problemas = []      # ["A", "B", "C", ...]
submissoes = []     # lista de dicionários com cada submissão
LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H"]


# ======================================================
#  FUNÇÕES AUXILIARES
# ======================================================

def calcular_pontuacao(nome_time):
    """Retorna (problemas_resolvidos, tempo_total) de um time."""
    resolvidos = 0
    tempo_total = 0

    for problema in problemas:
        erros_antes = 0
        minuto_aceito = None

        for sub in submissoes:
            if sub["time"] == nome_time and sub["problema"] == problema:
                if sub["veredito"] == "aceito":
                    minuto_aceito = sub["minuto"]
                    break        # para neste problema — já foi aceito
                else:
                    erros_antes += 1

        if minuto_aceito is not None:
            resolvidos += 1
            tempo_total += minuto_aceito + (erros_antes * 20)

    return resolvidos, tempo_total


def tem_campanha_perfeita(nome_time):
    """Retorna True se o time resolveu TODOS os problemas cadastrados."""
    if not problemas:
        return False
    resolvidos, _ = calcular_pontuacao(nome_time)
    return resolvidos == len(problemas)


def problemas_resolvidos_pelo_time(nome_time):
    """Retorna lista de letras dos problemas aceitos pelo time."""
    aceitos = []
    for problema in problemas:
        for sub in submissoes:
            if sub["time"] == nome_time and sub["problema"] == problema and sub["veredito"] == "aceito":
                aceitos.append(problema)
                break
    return aceitos


# ======================================================
#  OPÇÃO 1 — Cadastro de Times
# ======================================================

def cadastrar_times():
    if times:
        print("\n  Times já foram cadastrados! Volte ao menu.")
        return

    while True:
        entrada = input("\nQuantos times participarão? (mínimo 2): ").strip()
        if entrada.isdigit() and int(entrada) >= 2:
            quantidade = int(entrada)
            break
        print(" Informe um número inteiro maior ou igual a 2.")

    for i in range(quantidade):
        print(f"\n--- Time {i + 1} ---")

        while True:
            nome = input("Nome do time: ").strip()
            if not nome:
                print(" O nome não pode ser vazio.")
            elif nome in times:
                print(" Esse nome já existe. Escolha outro.")
            else:
                break

        membros = []
        for j in range(3):
            membro = input(f"  Membro {j + 1}: ").strip()
            membros.append(membro)

        times[nome] = membros
        print(f" Time '{nome}' cadastrado com sucesso!")


# ======================================================
#  OPÇÃO 2 — Cadastro de Problemas
# ======================================================

def cadastrar_problemas():
    if problemas:
        print("\n Problemas já foram cadastrados! Volte ao menu.")
        return

    while True:
        entrada = input(f"\nQuantos problemas terá a competição? (mínimo 1, máximo {len(LETRAS)}): ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= len(LETRAS):
            quantidade = int(entrada)
            break
        print(f" Informe um número entre 1 e {len(LETRAS)}.")

    for i in range(quantidade):
        problemas.append(LETRAS[i])

    print(f"\n Problemas cadastrados: {', '.join(problemas)}")


# ======================================================
#  OPÇÃO 3 — Registro de Submissão
# ======================================================

def registrar_submissao():
    if not times:
        print("\n⚠  Cadastre os times primeiro (Opção 1).")
        return
    if not problemas:
        print("\n⚠  Cadastre os problemas primeiro (Opção 2).")
        return

    # --- Nome do time ---
    nome_time = input("\nNome do time: ").strip()
    if nome_time not in times:
        print(" Time não encontrado.")
        return

    # --- Letra do problema ---
    letra = input("Letra do problema: ").strip().upper()
    if letra not in problemas:
        print(f"Problema '{letra}' não existe na competição.")
        return

    # --- Minuto da submissão ---
    entrada = input("Minuto da submissão (1–300): ").strip()
    if not entrada.isdigit() or not (1 <= int(entrada) <= 300):
        print(" Minuto inválido. Deve ser entre 1 e 300.")
        return
    minuto = int(entrada)

    # --- Veredito ---
    veredito = input("Veredito ('aceito' ou 'errado'): ").strip().lower()
    if veredito not in ("aceito", "errado"):
        print(" Veredito inválido. Use 'aceito' ou 'errado'.")
        return

    # --- Verificar se o problema já foi aceito antes ---
    for sub in submissoes:
        if sub["time"] == nome_time and sub["problema"] == letra and sub["veredito"] == "aceito":
            print(f" O time '{nome_time}' já resolveu o problema {letra}. Submissão rejeitada.")
            return

    submissoes.append({
        "time": nome_time,
        "problema": letra,
        "minuto": minuto,
        "veredito": veredito
    })
    print(f"✅ Submissão registrada: [{nome_time}] Problema {letra} — {veredito.upper()} no minuto {minuto}.")


# ======================================================
#  OPÇÃO 4 — Ranking
# ======================================================

def exibir_ranking():
    if not times:
        print("\n⚠  Nenhum time cadastrado.")
        return

    # Montar lista com pontuação de cada time
    classificacao = []
    for nome in times:
        resolvidos, tempo = calcular_pontuacao(nome)
        classificacao.append((nome, resolvidos, tempo))

    # Ordenar: mais problemas → menor tempo → ordem alfabética
    classificacao.sort(key=lambda x: (-x[1], x[2], x[0]))

    print("\n" + "=" * 55)
    print("             RANKING OFICIAL  ")
    print("=" * 55)
    print(f"{'Pos':<5} {'Time':<20} {'Problemas':>10} {'Tempo':>8}")
    print("-" * 55)

    for posicao, (nome, resolvidos, tempo) in enumerate(classificacao, start=1):
        print(f"{posicao:<5} {nome:<20} {resolvidos:>10} {tempo:>7}min")

    print("=" * 55)


# ======================================================
#  OPÇÃO 5 — Estatísticas
# ======================================================

def exibir_estatisticas():
    print("\n" + "=" * 50)
    print("       ESTATÍSTICAS")
    print("=" * 50)

    # --- R6: Problema mais fácil e mais difícil ---
    if not problemas:
        print("\n[Problemas] Nenhum problema cadastrado.")
    else:
        # Contar quantos times diferentes resolveram cada problema
        times_por_problema = {}
        for problema in problemas:
            times_que_resolveram = set()
            for sub in submissoes:
                if sub["problema"] == problema and sub["veredito"] == "aceito":
                    times_que_resolveram.add(sub["time"])
            times_por_problema[problema] = len(times_que_resolveram)

        # Filtrar somente problemas resolvidos por pelo menos 1 time
        resolvidos = {p: c for p, c in times_por_problema.items() if c > 0}

        if not resolvidos:
            print("\n[Dificuldade] Nenhum problema foi resolvido ainda.")
        else:
            max_resolvidos = max(resolvidos.values())
            min_resolvidos = min(resolvidos.values())

            mais_faceis = [p for p, c in resolvidos.items() if c == max_resolvidos]
            mais_dificeis = [p for p, c in resolvidos.items() if c == min_resolvidos]

            print(f"\n Problema(s) mais fácil(is): {', '.join(mais_faceis)}"
                  f" ({max_resolvidos} time(s))")
            print(f" Problema(s) mais difícil(is): {', '.join(mais_dificeis)}"
                  f" ({min_resolvidos} time(s))")

    # --- R7: Campanha perfeita ---
    print()
    if not times:
        print("[Campanha Perfeita] Nenhum time cadastrado.")
    elif not problemas:
        print("[Campanha Perfeita] Nenhum problema cadastrado.")
    else:
        times_perfeitos = [nome for nome in times if tem_campanha_perfeita(nome)]
        if times_perfeitos:
            print(f" Campanha perfeita: {', '.join(times_perfeitos)}")
        else:
            print(" Campanha perfeita: nenhum time resolveu todos os problemas.")

    # --- R8: Taxa de aceitação ---
    print()
    if not submissoes:
        print("[Taxa de Aceitação] Nenhuma submissão registrada.")
    else:
        total_subs = len(submissoes)
        aceitas = sum(1 for s in submissoes if s["veredito"] == "aceito")
        taxa = (aceitas / total_subs) * 100
        print(f" Taxa de aceitação geral: {taxa:.2f}%"
              f" ({aceitas} aceitas de {total_subs} submissões)")

    # --- R9: Menor tempo médio por problema ---
    print()
    if not times:
        print("[Tempo Médio] Nenhum time cadastrado.")
    else:
        melhor_time = None
        melhor_media = None

        for nome in times:
            resolvidos, tempo = calcular_pontuacao(nome)
            if resolvidos > 0:
                media = tempo / resolvidos
                if melhor_media is None or media < melhor_media:
                    melhor_media = media
                    melhor_time = nome

        if melhor_time is None:
            print("[Tempo Médio] Nenhum time pontuou ainda.")
        else:
            print(f" Menor tempo médio por problema: '{melhor_time}'"
                  f" com {melhor_media:.2f} min/problema")

    print("=" * 50)


# ======================================================
#  OPÇÃO 6 — Consultar Time
# ======================================================

def consultar_time():
    nome = input("\nNome do time a consultar: ").strip()

    if nome not in times:
        print(f" Time '{nome}' não encontrado.")
        return

    resolvidos_lista = problemas_resolvidos_pelo_time(nome)
    _, tempo_total = calcular_pontuacao(nome)
    perfeita = tem_campanha_perfeita(nome)

    print("\n" + "=" * 45)
    print(f"  Time: {nome}")
    print("=" * 45)
    print(f"  Membros : {', '.join(times[nome])}")

    if resolvidos_lista:
        print(f"  Resolvidos: {', '.join(resolvidos_lista)} ({len(resolvidos_lista)} problema(s))")
    else:
        print("  Resolvidos: nenhum ainda")

    print(f"  Tempo total: {tempo_total} minutos")
    print(f"  Campanha perfeita: {' SIM' if perfeita else ' NÃO'}")
    print("=" * 45)


# ======================================================
#  MENU PRINCIPAL
# ======================================================

def menu():
    while True:
        print("\n" + "=" * 45)
        print("OLIMPÍADA INTERNA DE PROGRAMAÇÃO")
        print("=" * 45)
        print("  1 - Cadastrar times")
        print("  2 - Cadastrar problemas")
        print("  3 - Registrar submissão")
        print("  4 - Exibir ranking")
        print("  5 - Exibir estatísticas")
        print("  6 - Consultar time")
        print("  0 - Sair")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_times()
        elif opcao == "2":
            cadastrar_problemas()
        elif opcao == "3":
            registrar_submissao()
        elif opcao == "4":
            exibir_ranking()
        elif opcao == "5":
            exibir_estatisticas()
        elif opcao == "6":
            consultar_time()
        elif opcao == "0":
            print("\n Encerrando o sistema. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# ======================================================
#  PONTO DE ENTRADA
# ======================================================

menu()