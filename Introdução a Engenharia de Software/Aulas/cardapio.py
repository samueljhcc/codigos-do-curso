# Dicionários com preços
hamburgueres = {
    1: ("Frango Bacon", 19.90),
    2: ("X-Burguer", 16.90),
    3: ("X-Salada", 9.90),
    4: ("X-Egg", 12.90),
    5: ("X-Calabresa", 11.90)
}

sucos = {
    1: ("Laranja", 5.00),
    2: ("Acerola", 4.00),
    3: ("Uva", 4.50),
    4: ("Morango", 8.00),
    5: ("Cajá", 4.00)
}


# Função para escolher
def pedido(nome):
    print(f"\nPedido de {nome}")

    h = int(input("Escolha o hamburguer (1-5): "))
    s = int(input("Escolha o suco (1-5): "))

    nome_h, preco_h = hamburgueres[h]
    nome_s, preco_s = sucos[s]

    total = preco_h + preco_s

    return {
        "nome": nome,
        "hamburguer": nome_h,
        "preco_h": preco_h,
        "suco": nome_s,
        "preco_s": preco_s,
        "total": total
    }


# Pedidos
yan = pedido("Yan")
esther = pedido("Esther")
theo = pedido("Theo")

# Mostrar contas individuais
print("\n===== CONTAS =====")
for pessoa in [yan, esther, theo]:
    print(f"{pessoa['nome']}: R$ {pessoa['total']:.2f}")

# Quem pagou mais pelo hamburguer
mais_caro = max([yan, esther, theo], key=lambda x: x["preco_h"])
menos_caro = min([yan, esther, theo], key=lambda x: x["preco_h"])

print(f"\nQuem pagou MAIS no hamburguer: {mais_caro['nome']} (R$ {mais_caro['preco_h']:.2f})")
print(f"Quem pagou MENOS no hamburguer: {menos_caro['nome']} (R$ {menos_caro['preco_h']:.2f})")