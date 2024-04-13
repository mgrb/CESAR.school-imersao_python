"""Questão 09. Controle de Contas Bancárias.

Crie um dicionário chamado contas para armazenar informações das contas
bancárias. As chaves serão os números das contas (por exemplo, "001", "002") e
os valores serão outros dicionários contendo as informações da conta: nome do
titular e saldo.

Implemente um menu com as seguintes opções:

● Digite 1 para criar uma nova conta. Solicite ao usuário o número da
conta, nome do titular e saldo inicial.
● Digite 2 para consultar o saldo de uma conta específica. Solicite ao
usuário o número da conta e exiba o saldo.
● Digite 3 para realizar um saque em uma conta. Solicite ao usuário o
número da conta e o valor a ser sacado. Certifique-se de que a conta
exista e que o saldo seja suficiente.
● Digite 4 para realizar um depósito em uma conta. Solicite ao usuário o
número da conta e o valor a ser depositado.
● Digite 5 para sair do programa.

Após cada operação, exiba uma mensagem apropriada informando o resultado
da operação (por exemplo, "Conta criada com sucesso", "Saldo da conta: x.x",
"Saque realizado com sucesso", "Depósito realizado com sucesso"). Garanta que
o programa seja executado em um loop até que o usuário escolha a opção 5 para
sair. Certifique-se de que o programa lide adequadamente com casos em que o
usuário consulta, saca ou deposita em uma conta que não existe.
"""

if __name__ == '__main__':
    print('\n\n****\n Questão 09. Controle de Contas Bancárias\n****\n')

    contas_bancarias = {}

    while True:
        print(f'\n {"=" * 10} \n Controle de Contas Bancárias \n {"-" * 10} \n')
        print('1. Criar nova conta')
        print('2. Consultar saldo')
        print('3. Realizar saque')
        print('4. Realizar depósito')
        print('5. Sair')

        opcao = input('Digite a opção desejada: ')

        match opcao:
            case '1':
                num_conta = input('Número da conta: ')
                nome_titular = input('Nome do titular: ')
                saldo = float(input('Saldo inicial: '))
                contas_bancarias[num_conta] = {
                    'titular': nome_titular,
                    'saldo': saldo,
                }
                print('Conta criada com sucesso.')

            case '2':
                num_conta = input('Número da conta: ')
                conta = contas_bancarias.get(num_conta)
                print(f'Saldo da conta: {conta["saldo"]}') if conta else print(
                    'Conta não encontrada.',
                )

            case '3':
                num_conta = input('Número da conta: ')
                saque = float(input('Valor a ser sacado: '))
                conta = contas_bancarias.get(num_conta)
                if conta:
                    if conta['saldo'] >= saque:
                        conta['saldo'] -= saque
                        print('Saque realizado com sucesso.')
                    else:
                        print('Saldo insuficiente.')
                else:
                    print('Conta não encontrada.')

            case '4':
                num_conta = input('Número da conta: ')
                deposito = float(input('Valor a ser depositado: '))
                conta = contas_bancarias.get(num_conta)
                if conta:
                    conta['saldo'] += deposito
                    print('Depósito realizado com sucesso.')
                else:
                    print('Conta não encontrada.')

            case '5':
                print('Programa finalizado.')
                break
