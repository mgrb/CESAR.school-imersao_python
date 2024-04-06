"""Questão 04. Petshop.

Um petshop atende 10 cachorros por tarde. Faça um programa que solicite ao
usuário o código do serviço efetuado: (1 - banho; 2 - tosa; 3 - banho e tosa;
4- outros). Por fim, exiba a quantidade de solicitações para cada um deles.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Petshop')

    # Inicializa as variáveis
    qtd_banho = 0
    qtd_tosa = 0
    qtd_banho_tosa = 0
    qtd_outros = 0
    qtd_servicos = 0

    # Loop infinito
    while qtd_servicos < 10:
        servico = int(
            input(
                'Digite o código do serviço (1 - banho; 2 - tosa; 3 - banho e tosa; 4 - outros): ',
            ),
        )
        match servico:
            case 1:
                qtd_banho += 1
            case 2:
                qtd_tosa += 1
            case 3:
                qtd_banho_tosa += 1
            case 4:
                qtd_outros += 1
            case _:
                print('Código inválido! Digite um código válido.')
                continue

        qtd_servicos += 1

    print(f'Quantidade de banhos: {qtd_banho}')
    print(f'Quantidade de tosas: {qtd_tosa}')
    print(f'Quantidade de banhos e tosas: {qtd_banho_tosa}')
    print(f'Quantidade de outros: {qtd_outros}')
