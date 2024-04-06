"""Questão 3. Controle de Estoque.

Uma loja deseja criar um sistema de controle de estoque. O usuário deve inserir
o nome do produto e a quantidade. Se a quantidade for negativa, o programa deve
informar um erro e pedir novamente. Após cada inserção, o sistema solicitará um
novo nome ou o usuário informará “FIM” para encerrar o sistema. Por fim, o
sistema deverá apresentar a quantidade de tipos de produtos inseridos.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Controle de Estoque')

    # Inicializa as variáveis
    qtd_produtos = 0
    produto = ''
    qtd = 0

    # Loop infinito
    while produto != 'FIM':
        produto = str.upper(input('Digite o nome do produto: '))
        if produto != 'FIM':
            qtd = int(input('Digite a quantidade do produto: '))
            if qtd < 0:
                print('Não é possível cadastro de estoque negativo.')
            else:
                qtd_produtos += 1

    print(f'Tipos de produtos cadastrados: {qtd_produtos}')
