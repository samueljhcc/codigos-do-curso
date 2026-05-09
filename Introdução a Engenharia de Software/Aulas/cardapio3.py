# Menu da Lanchonete
menu_hamburguer = {
    "Frango Bacon": 19.90,
    "X-Burguer": 16.90,
    "X-Salada": 9.90,
    "X-Egg": 12.90,
    "X-Calabresa": 11.90
}

menu_suco = {
    "Laranja": 5.00,
    "Acerola": 4.00,
    "Uva": 4.50,
    "Morango": 8.00,
    "Cajá": 4.00
}

# Exibir o menu
print("=== Menu Rodrigo Lanches ===")
print("Hambúrgueres:")
for item, preco in menu_hamburguer.items():
    print(f"{item} - R$ {preco:.2f}")

print("\nSucos (300ml):")
for item, preco in menu_suco.items():
    print(f"{item} - R$ {preco:.2f}")

# Solicitar pedidos
clientes = ["Yan", "Esther", "Theo"]
pedidos = {}

for cliente in clientes:
    print(f"\nPedido de {cliente}:")
    hamburguer = input("Escolha o hambúrguer: ")
    suco = input("Escolha o suco: ")
    pedidos[cliente] = {
        "hamburguer": hamburguer,
        "suco": suco,
        "total": menu_hamburguer[hamburguer] + menu_suco[suco]
    }

# Mostrar contas individuais
print("\n=== Contas Individuais ===")
for cliente, dados in pedidos.items():
    print(f"{cliente}: R$ {dados['total']:.2f}")

# Quem pagou mais/menos pelo hambúrguer
mais_caro = max(pedidos, key=lambda c: menu_hamburguer[pedidos[c]["hamburguer"]])
mais_barato = min(pedidos, key=lambda c: menu_hamburguer[pedidos[c]["hamburguer"]])

print(f"\n{mais_caro} pagou mais pelo hambúrguer.")
print(f"{mais_barato} pagou menos pelo hambúrguer.")

# Esther pede outro suco (Morango)
extra = menu_suco["Morango"]
print(f"\nEsther pagará R$ {extra:.2f} a mais pelo novo suco.")
