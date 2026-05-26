numero = int(input("Digite um número positivo: "))

while numero <= 0:
    print("Número inválido!")
    numero = int(input("Digite um número positivo: "))

contador = 1

while contador <= numero:

    if contador % 3 == 0:
        print("Pula!")
    else:
        print(contador)

    contador += 1