total = int(input('Quantos litros cabem no tanque? '))
atual = float(input('Quantos litros tem no tanque?'))
preco = float(input('Preço do combustível: R$'))

falta = total-atual
print('Para completar o tanque, é necessário: R${:.2f}'.format(falta*preco))

c_medio = 10.5
print('Com o tanque cheio, o carro irá rodar {} Quilômetros.'.format(total*c_medio))