# Exibir o cardápio completo da lanchonete
print('Cardápio da Lanchonete Rodrigo Lanches:')

print('Hamburguers:')
print(
    '1 - Frango Bacon - R$19,90'
    '2 - X-Burgger - R$16,90'
    '3 - X-Salada - R$9,90'
    '4 - X-Egg - R$12,90'
    '5 - X-Calabresa - R$11,90'
)

print('Sucos:')
print(
    '1 - Suco de Laranja - R$5,00'
    '2 - Suco de Acerola - R$4,00'
    '3 - Suco de Uva - R$4,50'
    '4 - Suco de Morango - R$8,00'
    '5 - Suco de Cajá - R$4,00'
)

# Definir a tabela de preços que o programa vai utilizar.
hamburgueres = {
    1: ('Frango Bacon', 19.90),
    2: ('X-Burguer', 16.90),
    3: ('X-Salada', 9.90),
    4: ('X-Egg', 12.90),
    5: ('X-Calabresa', 11.90)
}

sucos = {
    1: ('Laranja', 5.00),
    2: ('Acerola', 4.00),
    3: ('Uva', 4.50),
    4: ('Morango', 8.00),
    5: ('Cajá', 4.00)
}

# Criar uma função para descobrir qual foi o pedido da pessoa.
def pedido(nome):
    print(f'\nPedido de {nome}')

    h = int(input('Escolha o hamburguer (1-5): '))
    s = int(input('Escolha o suco (1-5): '))

    nome_h, preco_h = hamburgueres[h]
    nome_s, preco_s = sucos[s]

    total = preco_h + preco_s

    return {
        'nome': nome,
        'hamburguer': nome_h,
        'preco_h': preco_h,
        'suco': nome_s,
        'preco_s': preco_s,
        'total': total
    }


# Repassar os pedidos.
yan = pedido('Yan')
esther = pedido('Esther')
theo = pedido('Theo')

# Exibir quanto ficou para cada um.
print('\n===== CONTAS =====')
for pessoa in [yan, esther, theo]:
    print(f"{pessoa['nome']}: R$ {pessoa['total']:.2f}")

# Exibir quem pagou mais e quem pagou menos.
mais_caro = max([yan, esther, theo], key=lambda x: x["preco_h"])
menos_caro = min([yan, esther, theo], key=lambda x: x["preco_h"])

print(f"\nQuem pagou MAIS no hamburguer: {mais_caro['nome']} (R$ {mais_caro['preco_h']:.2f})")
print(f"Quem pagou MENOS no hamburguer: {menos_caro['nome']} (R$ {menos_caro['preco_h']:.2f})")

# Suco extra de Esther.
print('Como Esther pediu um suco extra de morango, então pagará R$8 a mais, totalizando R${:.2f}'.format(pedido("Esther")["total"] + 8))