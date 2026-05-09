n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >= 7:
    print('Aprovado!')
elif media < 3.5:
    print('Reprovado!')