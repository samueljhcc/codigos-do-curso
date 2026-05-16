print("=" * 40)
print("   BEM-VINDO AO CASTELO MEDIEVAL")
print("=" * 40)

visitantes_aprovados = 0
senha_correta = "dragao123"

senha = input("\nDigite a senha (ou 'encerrar' para finalizar): ")

while senha != "encerrar":
    if senha == senha_correta:
        print("Bem-vindo ao castelo!")
        visitantes_aprovados += 1
    else:
        print("Senha incorreta. Próximo!")

    senha = input("\nDigite a senha (ou 'encerrar' para finalizar): ")

print(f"\n{'=' * 40}")
print(f"Expediente encerrado!")
print(f"Total de visitantes que entraram: {visitantes_aprovados}")
print(f"{'=' * 40}")