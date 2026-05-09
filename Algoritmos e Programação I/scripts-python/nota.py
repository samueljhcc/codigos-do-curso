nota1 = float(input('Qual a sua primeira nota ?'))
nota2 = float(input('Qual a sua segunda nota ?'))
nota3 = float(input('Qual a sua terceira nota ?'))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print('Aprovado!')
elif media < 7 and media >= 3.5:
    print('Faltou {:.2f} para você ser aprovado!'.format(7 - media))
    quarta = float(input('Qual foi a sua nota no 4ª prova? '))
    nova_media = (((media*6) + (quarta*4)) / 10)
    if nova_media >= 5:
        print('Sua nova média foi de {:.2f} e você está aprovado!'.format(nova_media))
    else:
        print('Sua nova média foi de {:.2f} e você está reprovado!'.format(nova_media))
else:
    print('Reprovado!')