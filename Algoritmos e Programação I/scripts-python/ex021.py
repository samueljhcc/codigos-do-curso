s_inicial = 1000
operacoes = 0 

while s_inicial != 0:
    operacoes += 1
    s_inicial = 1000
    print(' 1 - Deposito', '\n 2 - Saque', '\n 3 - Extrato', '\n 4 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        valor = float(input('Digite o valor do depósito: '))
        s1 = s_inicial + valor
        print('Depósito realizado com sucesso! Saldo atual: R$ {:.2f}'.format(s1))
    elif opcao == 2:
        valor = float(input('Digite o valor do saque: '))
        s2 = s1 - valor
        if valor > s1:
            print('Saldo insuficiente para realizar o saque. Saldo atual: R$ {:.2f}'.format(s_inicial))
        else:
            s2 = s1 - valor
            print('Saque realizado com sucesso! Saldo atual: R$ {:.2f}'.format(s2))
    elif opcao == 3:
        print('Saldo atual: R$ {:.2f}'.format(s2))
    elif opcao == 4:
        print('Saindo do sistema. Obrigado por usar nossos serviços!')
        break

print('Número de operações realizadas: {}'.format(operacoes))