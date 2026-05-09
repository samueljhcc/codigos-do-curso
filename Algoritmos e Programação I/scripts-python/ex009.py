nome = input('Qual é o nome do aluno?')

nota1 = float(input('Qual foi a primeira nota do aluno?'))
nota2 = float(input('Qual foi a segunda nota do aluno?'))
nota3 = float(input('Qual foi a terceira nota do aluno?'))

print('O nome do aluno é {}, e ele obteve a média {:.2f}'.format(nome, (nota1+nota2+nota3)/3))